from flask_sqlalchemy import SQLAlchemy
import re

db = SQLAlchemy()

association_table = db.Table(
    "association",
    db.Model.metadata,
    db.Column("party_id", db.Integer, db.ForeignKey("parties.id")),
    db.Column("user_id", db.Integer, db.ForeignKey("users.id"))
)

class Party(db.Model):
    __tablename__ = "parties"
    id = db.Column(db.Integer, primary_key=True)
    host = db.Column(db.String, nullable=False)
    photo = db.relationship("ImgEvent", cascade="delete")
    location = db.Column(db.String, nullable=False)
    dateTime = db.Column(db.String, nullable=False)
    users = db.relationship("User", secondary=association_table,back_populates="parties")

    def __init__(self, **kwargs):
        self.host = kwargs.get("host")
        self.location = kwargs.get("location")
        self.dateTime = kwargs.get("dateTime")
        self.users = kwargs.get("attendees")

    def serialize(self):
        return {
            "id": self.id,
            "host":self.host,
            "location":self.location,
            "dateTime":self.dateTime,
            "attendees":[user.sub_serialize() for user in self.users]
        }
    def sub_serialize(self):
        return {
            "id": self.id,
            "host":self.host,
            "location":self.location,
            "dateTime":self.dateTime
        }

    def serialize_img_id(self):
        return {
            "photo": [i.serialize_id() for i in self.photo]
        }

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    photo = db.relationship("Img", cascade="delete")
    age = db.Column(db.String, nullable=False)
    parties = db.relationship(
        "Party",
        secondary=association_table,
        back_populates = "users"
    )

    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.email = kwargs.get("email")
        self.age = kwargs.get("age")
        
    def serialize(self):
        return {
            "id":self.id,
            "name":self.name,
            "email":self.email,
            "age":self.age,
            "parties":[party.sub_serialize() for party in self.parties]
        }
    def sub_serialize(self):
        return {
            "id":self.id,
            "name":self.name,
            "email":self.email,
            "age":self.age
        }
    
    def serialize_img_id(self):
        return {
            "photo": [i.serialize_id() for i in self.photo]
        }
        
class Img(db.Model):
    __tablename__ = "image"
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.Text, unique=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    
    def __init__(self, **kwargs):
        self.img = kwargs.get("img")
        self.name = kwargs.get("name")
        self.mimetype = kwargs.get("mimetype")
        self.user_id = kwargs.get("user_id")
    
    def serialize_id(self):
        return {
            "id": self.id
        }

class ImgEvent(db.Model):
    __tablename__ = "eventImage"
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.Text, unique=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)
    party_id = db.Column(db.Integer, db.ForeignKey("parties.id"))
    
    def __init__(self, **kwargs):
        self.img = kwargs.get("img")
        self.name = kwargs.get("name")
        self.mimetype = kwargs.get("mimetype")
        self.party_id = kwargs.get("party_id")
    
    def serialize_id(self):
        return {
            "id": self.id
        }
