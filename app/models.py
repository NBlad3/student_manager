from app import db

class Dog(db.Model):
    __tablename__ = "dogs"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(255), nullable = True)
    age = db.Column(db.Integer, nullable = True)

class Cat(db.Model):
    __tablename__ = "cats"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(255), nullable = True)
    age = db.Column(db.Integer, nullable = True)

