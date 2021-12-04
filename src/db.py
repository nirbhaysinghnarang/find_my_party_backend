from flask_sqlalchemy import SQLAlchemy

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
    location = db.Column(db.String, nullable=False)
    photoURL = db.Column(db.String, nullable=False)
    dateTime = db.Column(db.String, nullable=False)
    theme = db.Column(db.String, nullable=False)
    users = db.relationship(
                    "User",
                    secondary=association_table,
                    back_populates="parties"
                )

    def __init__(self, **kwargs):
        self.host = kwargs.get("host")
        self.location = kwargs.get("location")
        self.photoURL = kwargs.get("photoURL")
        self.dateTime = kwargs.get("dateTime")
        self.users = kwargs.get("attendees")
        self.theme = kwargs.get("theme")

    def serialize(self):
        return {
            "id": self.id,
            "host":self.host,
            "location":self.location,
            "photoURL":self.photoURL,
            "dateTime":self.dateTime,
            "theme": self.theme,
            "attendees":[user.sub_serialize() for user in self.users]
        }
    def sub_serialize(self):
        return {
            "id": self.id,
            "host":self.host,
            "location":self.location,
            "photoURL":self.photoURL,
            "dateTime":self.dateTime,
            "theme": self.theme
        }

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    photoURL = db.Column(db.String, nullable=False)
    parties = db.relationship(
        "Party",
        secondary=association_table,
        back_populates = "users"
    )

    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.email = kwargs.get("email")
        self.photoURL = kwargs.get("photoURL")

    def serialize(self):
        return {
            "id":self.id,
            "name":self.name,
            "email":self.email,
            "photoURL":self.photoURL,
            "parties":[party.sub_serialize() for party in self.parties]
        }
    def sub_serialize(self):
        return {
            "id":self.id,
            "name":self.name,
            "email":self.email,
            "photoURL":self.photoURL,
        }
