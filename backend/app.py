import os
from flask import Flask, request
from models import Venue, Movie
from config import LocalDevementConfig
from database import db
from flask_restful import Api
# from tasks import send_mail
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from api import UserResource, UserListResource, VenueResource, VenueListResource, MovieResource, MovieListResource, BookingResource, BookingListResource
from flask_cors import CORS
import workers
# import tasks
import redis

app = None
api = None
jwt = None
celery = None
cache = None

def create_app():
    app = Flask(__name__)
    app.secret_key='ticketshow'
    if os.getenv('ENV', 'development') == 'production':
        raise Exception('Production environment not configured yet')
    else:
        print('Starting in development mode')
        app.config.from_object(LocalDevementConfig)
    app.app_context().push()
    db.init_app(app)
    with app.app_context():
        # db.drop_all()
        db.create_all()

    jwt = JWTManager(app)

    api = Api(app)

    # create celery 
    celery = workers.celery

    celery.conf.update(
        broker_url=app.config["CELERY_BROKER_URL"],
        result_backend=app.config["CELERY_RESULT_BACKEND"],
    )

    celery.Task = workers.ContextTask
    app.app_context().push()


    redis_connection = redis.StrictRedis(
        host=app.config['REDIS_HOST'],
        port=app.config['REDIS_PORT'],
        db=app.config['REDIS_DB']
    )
    app.redis = redis_connection
    app.app_context().push()

    from cache import cache
    cache.init_app(app)
    app.app_context().push()

    return app, api, jwt, celery, cache



from models import User, Role
app, api, jwt, celery, cache = create_app()

# find admin from database having User, Role model with many to many relationship
def isAdminPresent():
    admin = User.query.all()
    if len(admin) == 0:
        return False
    else:
        for i in admin:
            for j in i.roles:
                if j.name == 'admin':
                    return True
        return False

# create admin user if not present
def createAdmin():
    if isAdminPresent() == False:
        admin_role = Role(name='admin')
        db.session.add(admin_role)
        db.session.commit()
        admin = User(name='Shalix' ,email='admin@showbookig.com', password='admin', active=True)
        admin.roles.append(admin_role)
        db.session.add(admin)
        db.session.commit()
    else:
        print('Admin already present')
        return

with app.app_context():
    createAdmin()

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']
    user = User.query.filter_by(email=email).first()
    if user and user.password == password:
        access_token = create_access_token(identity=user.id)
        # send_mail("Welcome to BookMyShow Login", "Welcome", user.email)
        return {'access_token': access_token}, 200
    return {'message': 'Invalid credentials'}, 401

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected_route():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    return {'message': f'Hello, {user.name}! You have access to this protected route.'}  

@app.route('/search', methods=['GET'])
def search():
    name = request.args.get('name')
    venues = Venue.query.filter(Venue.name.contains(name)).all()
    movies = Movie.query.filter(Movie.title.contains(name)).all()
    if venues or movies:
        return {'venue': [venue.json() for venue in venues], 'movie': [movie.json() for movie in movies]}, 200
    else:
        return {'message': 'No result found'}, 404
    
@app.route('/export_theatre_csv', methods=['POST'])
def export_theatre_csv():
    theatre_id = request.form.get('theatre_id')  
    export_theatre_csv.delay(theatre_id)
    return jsonify({'message': 'Export job triggered! You will receive an email once it\'s done.'})


# Add API resources
api.add_resource(UserResource, '/users/<int:id>')
api.add_resource(UserListResource, '/users')
api.add_resource(VenueResource, '/venues/<int:id>')
api.add_resource(VenueListResource, '/venues')
api.add_resource(MovieResource, '/movies/<int:id>')
api.add_resource(MovieListResource, '/movies')
api.add_resource(BookingResource, '/bookings/<int:id>')
api.add_resource(BookingListResource, '/bookings')


if __name__ == '__main__':
    CORS(app)
    app.run(debug=True)