from ast import Pass
from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename
from wtforms import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import (
    InputRequired,
    Length,
    Email,
    EqualTo,
    ValidationError,
)

from .models import User

class SearchForm(FlaskForm):
    search_query = StringField(
        "Query", validators=[InputRequired(), Length(min=1, max=100)]
    )
    submit = SubmitField("Search")

class RegistrationForm(FlaskForm):
    username = StringField(
        "Username", validators=[InputRequired(), Length(min=1, max=40)]
    )
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired()])
    confirm_password = PasswordField(
        "Confirm Password", validators=[InputRequired(), EqualTo("password")]
    )
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user = User.objects(username=username.data).first()
        if user is not None:
            raise ValidationError("Username is taken")

    def validate_email(self, email):
        user = User.objects(email=email.data).first()
        if user is not None:
            raise ValidationError("Email is taken")


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(min=1, max=40)])
    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Log In")

class RecipeForm(FlaskForm):
    title = StringField("Title", validators=[InputRequired(), Length(min=1, max=100)])
    description = TextAreaField(
        "Description", validators=[InputRequired(), Length(min=1, max=1000)]
    )
    ingredients = TextAreaField(
        "Ingredients", validators=[InputRequired(), Length(min=1)]
    )
    instructions = TextAreaField(
        "Instructions", validators=[InputRequired(), Length(min=1)]
    )
    image = FileField(
        "Image",
        validators=[
            FileRequired(),
            FileAllowed(["jpg", "png"], "Images only!"),
        ],
    )
    submit = SubmitField("Post Recipe")

class UpdateUsernameForm(FlaskForm):
    username = StringField(
        "New Username", validators=[InputRequired(), Length(min=1, max=40)]
    )
    submit_username = SubmitField("Update Username") 

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.objects(username=username.data).first()
            if user is not None:
                raise ValidationError("Username is taken")

class UpdateProfilePicForm(FlaskForm):
    picture = FileField(
        "Profile Picture",
        validators=[
            FileRequired(),
            FileAllowed(["jpg", "png"], "Images only!"),
        ],
    )
    submit_picture = SubmitField("Update Profile Picture")

class DeleteRecipeForm(FlaskForm):
    submit = SubmitField("Delete Recipe")