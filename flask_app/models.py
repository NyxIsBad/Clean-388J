from flask_login import UserMixin
from datetime import datetime
from . import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.objects(username=user_id).first()

class User(db.Document, UserMixin):
    username = db.StringField(required=True, unique=True, min_length=1, max_length=40)
    email = db.StringField(required=True, unique=True)
    password = db.StringField(required=True) # slow-hashed passwords
    profile_pic = db.ImageField()
    email_confirmed = db.BooleanField(default=False)

    # Returns unique string identifying our object
    def get_id(self):
        # the username is unique to each user
        return self.username
    

class Recipe(db.Document):
    recipe_id = db.IntField(required=True, unique=True)
    title = db.StringField(required=True, min_length=1, max_length=100)
    description = db.StringField(required=True, min_length=1, max_length=1000)
    ingredients = db.StringField(required=True, min_length=1)
    instructions = db.StringField(required=True, min_length=1)
    image = db.ImageField()
    date_posted = db.DateTimeField(default=datetime.now)
    author = db.ReferenceField(User, required=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title