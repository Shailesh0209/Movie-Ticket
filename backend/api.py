from datetime import datetime
from flask_restful import Api, Resource, reqparse
from models import User, Role, Venue, Movie, Booking
# from tasks import send_mail
from cache import cache


user_parser = reqparse.RequestParser()
user_parser.add_argument('name', type=str, required=True, help='Name cannot be blank')
user_parser.add_argument('email', type=str, required=True, help='Email cannot be blank')
user_parser.add_argument('password', type=str, required=True, help='Password cannot be blank') 
venue_parser = reqparse.RequestParser()
venue_parser.add_argument('name', type=str, required=True, help='Name cannot be blank')
venue_parser.add_argument('address', type=str, required=True, help='Address cannot be blank')
movie_parser = reqparse.RequestParser()
movie_parser.add_argument('title', type=str, required=True, help='Title cannot be blank')
movie_parser.add_argument('start_timing', type=str, required=True, help='Start timing cannot be blank')
movie_parser.add_argument('end_timing', type=str, required=True, help='End timing cannot be blank')
movie_parser.add_argument('ticket_price', type=int, required=True, help='Ticket price cannot be blank')
movie_parser.add_argument('venue_id', type=int, required=False, help='Venue id cannot be blank')
booking_parser = reqparse.RequestParser()
booking_parser.add_argument('user_id', type=int, required=True, help='User id cannot be blank')
booking_parser.add_argument('movie_id', type=int, required=True, help='Movie id cannot be blank')
booking_parser.add_argument('seats', type=str, required=True, help='Seats cannot be blank')

class UserResource(Resource):    
    def get(self, id):
        user = User.get_by_id(id)
        return user.json(), 200
    
    def put(self, id):
        args = user_parser.parse_args()
        user = User.get_by_id(id)
        user.name = args['name']
        user.email = args['email']
        user.password = args['password']
        user.update()
        return user.json(), 200
    
    def delete(self, id):
        user = User.get_by_id(id)
        user.delete()
        return 'deleted', 200

class UserListResource(Resource):
    def post(self):
        args = user_parser.parse_args()
        user_role = Role.get_by_name('user')
        if user_role is None:
            user_role = Role(name='user')
            user_role.save()
        user = User(name=args['name'], email=args['email'], password=args['password'], active=True)
        user.roles.append(user_role)
        user.save()
        send_mail("Welcome to BookMyShow", "Welcome", user.email)
        return user.json(), 201   
    
    def get(self):
        users = User.getUserList()
        return [user.json() for user in users], 200


class VenueResource(Resource):
    def get(self, id):
        venue = Venue.get_by_id(id)
        return venue.json(), 200
    
    def put(self, id):
        args = venue_parser.parse_args()
        venue = Venue.get_by_id(id)
        venue.name = args['name']
        venue.address = args['address']
        venue.update()
        return venue.json(), 200
    
    def delete(self, id):
        venue = Venue.get_by_id(id)
        venue.delete()
        return 'deleted', 200
    
class VenueListResource(Resource):
    def post(self):
        args = venue_parser.parse_args()
        venue = Venue(name=args['name'], address=args['address'])
        venue.save()
        return venue.json(), 201
    
    @cache.cached(timeout=50)
    def get(self):
        venues = Venue.getVenueList()
        return [venue.json() for venue in venues], 200
    
class MovieResource(Resource):
    @cache.cached(timeout=50)
    def get(self, id):
        movie = Movie.get_by_id(id)
        return movie.json(), 200
    
    def put(self, id):
        args = movie_parser.parse_args()
        movie = Movie.get_by_id(id)
        print(movie.title)
        movie.title = args['title']
        movie.start_timing = args['start_timing']
        movie.end_timing = args['end_timing']
        movie.ticket_price = args['ticket_price']
        movie.update()
        return movie.json(), 200
    
    def delete(self, id):
        movie = Movie.get_by_id(id)
        movie.delete()
        return 'deleted', 200
    
class MovieListResource(Resource):
    def post(self):
        args = movie_parser.parse_args()
        movie = Movie(title=args['title'], start_timing=args['start_timing'], end_timing=args['end_timing'], ticket_price=args['ticket_price'])
        movie.save()
        print(args['venue_id'])
        venue = Venue.get_by_id(args['venue_id'])
        venue.movies.append(movie)
        venue.update()
        print(venue.name)
        # venue.movies.append(movie)
        return movie.json(), 201
    
    def get(self):
        movies = Movie.getMovieList()
        return [movie.json() for movie in movies], 200
    
class BookingResource(Resource):
    def get(self, id):
        booking = Booking.get_by_id(id)
        return booking.json(), 200
    
    def put(self, id):
        args = booking_parser.parse_args()
        booking = Booking.get_by_id(id)
        booking.user_id = args['user_id']
        booking.movie_id = args['movie_id']
        booking.total_price = args['total_price']
        booking.seats = args['seats']
        booking.timing = args['timing']
        booking.update()
        return booking.json(), 200
    
    def delete(self, id):
        booking = Booking.get_by_id(id)
        booking.delete()
        return 'deleted', 200
    
class BookingListResource(Resource):
    def post(self):
        args = booking_parser.parse_args()
        print(args['user_id'])
        print(args['movie_id'])
        print(args['seats'])
        movie = Movie.get_by_id(args['movie_id'])
        user = User.get_by_id(args['user_id'])
        booking = Booking()
        booking.user_id = args['user_id']
        booking.movie_id = args['movie_id']
        booking.seats = args['seats']
        booking.total_price = int(movie.ticket_price) * len(args['seats'].split(','))
        booking.timing = movie.start_timing
        booking.save()
        # send_mail("Booking Confirmed", "Booking", user.email)
        return booking.json(), 201
    def get(self):
        bookings = Booking.getBookingList()
        return [booking.json() for booking in bookings], 200
    
    