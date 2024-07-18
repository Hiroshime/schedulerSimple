from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    birthdate = db.Column(db.DateTime,nullable=False)
    registerdate = db.Column(db.DateTime,nullable=False)
    email = db.Column(db.String(25),nullable=True)
    phone = db.Column(db.String(25),nullable=True)


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    schedule = db.Column(db.DateTime,nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    status = db.Column(db.String(30), nullable=False)
    user = db.relationship('User',backref=db.backref('sessions',lazy=True))
    registerdate = db.Column(db.DateTime, nullable=False)

