from datetime import datetime
from database import db
from flask_login import UserMixin
from flask_security import RoleMixin

# Define models

roles_users = db.Table('roles_users',
                          db.Column('user_id', db.Integer(),
                                    db.ForeignKey('user.id')),
                            db.Column('role_id', db.Integer(),
                                        db.ForeignKey('role.id')))
class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True, default='user')

    def __repr__(self):
        return '<Role %r>' % self.name
    
    def save(self, ):
        db.session.add(self)
        db.session.commit()
        return self
    
    def delete(self, ):
        db.session.delete(self)
        db.session.commit()
        return self
    
    def update(self, ):
        db.session.commit()
        return self
    
    def get_by_id(id):
        return Role.query.get(id)
    
    def get_by_name(name):
        return Role.query.filter_by(name=name).first()
    
    def getRoleList():
        return Role.query.all()
    
    def json(self):
        return {
            'id': self.id,
            'name': self.name
        }

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    bookings = db.relationship('Booking', backref='user', lazy=True)
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))
    
    def __repr__(self):
        return '<User %r>' % self.name
    
    def save(self, ):
        db.session.add(self)
        db.session.commit()
        return self
    
    def delete(self, ):
        db.session.delete(self)
        db.session.commit()
        return self
    
    def update(self, ):
        db.session.commit()
        return self
    
    def get_by_id(id):
        return User.query.get(id)
    
    def getUserList():
        return User.query.all()
    
    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'active': self.active,
            'role': self.roles[0].json()['name']
        }
    
venue_movie = db.Table('venue_movie',
                            db.Column('venue_id', db.Integer(),
                                        db.ForeignKey('venue.id')),
                            db.Column('movie_id', db.Integer(),
                                        db.ForeignKey('movie.id')))

class Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    address = db.Column(db.String(255))
    movies = db.relationship('Movie', secondary=venue_movie,
                            backref=db.backref('venues', lazy='dynamic'))
    
    def __repr__(self):
        return '<Venue %r>' % self.name
    
    def save(self, ):
        db.session.add(self)
        db.session.commit()
        return self
    
    def delete(self, ):
        db.session.delete(self)
        db.session.commit()
        return self
    
    def update(self, ):
        db.session.commit()
        return self
    
    def get_by_id(id):
        return Venue.query.get(id)
    
    def getVenueList():
        return Venue.query.all()
    
    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'movies': [movie.json() for movie in self.movies]
        }

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    start_timing = db.Column(db.String(255))
    end_timing = db.Column(db.String(255))
    ticket_price = db.Column(db.Integer)
    bookings = db.relationship('Booking', backref='movie', lazy=True)
    def __repr__(self):
        return '<Movie %r>' % self.title

    def save(self, ):
        db.session.add(self)
        db.session.commit()
        return self
    
    def delete(self, ):
        db.session.delete(self)
        db.session.commit()
        return self
    
    def update(self, ):
        db.session.commit()
        return self
    
    def get_by_id(id):
        return Movie.query.get(id)
    
    def getMovieList():
        return Movie.query.all()
    
    def json(self):
        return {
            'id': self.id,
            'title': self.title,
            'start_timing': self.start_timing,
            'end_timing': self.end_timing,
            'ticket_price': self.ticket_price
        }
    
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    total_price = db.Column(db.Integer)
    seats = db.Column(db.String(255))
    timing = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return '<Booking %r>' % self.id

    def save(self, ):
        db.session.add(self)
        db.session.commit()
        return self
    
    def delete(self, ):
        db.session.delete(self)
        db.session.commit()
        return self
    
    def update(self, ):
        db.session.commit()
        return self
    
    def get_by_id(id):
        return Booking.query.get(id)
    
    def getBookingList():
        return Booking.query.all()
    
    def json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'movie_id': self.movie_id,
            'total_price': self.total_price,
            'seats': self.seats,
            'timing': self.timing
        }