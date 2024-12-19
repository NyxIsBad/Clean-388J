from flask import Blueprint, redirect, url_for, render_template, flash, request
from flask_login import current_user, login_required, login_user, logout_user
from flask_mail import Message
import base64
from ... import bcrypt, mail
from werkzeug.utils import secure_filename
from ...forms import RegistrationForm, LoginForm, UpdateUsernameForm, UpdateProfilePicForm, DeleteRecipeForm
from ...models import User, Recipe
from ...utils import get_b64_img, generate_token, confirm_token

users = Blueprint("users", __name__)

""" ************ User Management views ************ """

@users.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("recipes.index"))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        user.save()

        token = generate_token(user.email)
        verify_url = url_for("users.verify_email", token=token, _external=True)
        msg = Message(
            "Email Verification",
            recipients=[user.email]
        )
        msg.body = f"Click the link to verify your email: {verify_url}"

        try:
            mail.send(msg)
            flash("Account created successfully. Please check your email to verify your account.", "success")
        except Exception as e:
            flash("There was an error sending a verification email email. Please try again later.", "danger")
            print(f"Error sending email: {e}")

        return redirect(url_for("users.login"))
    return render_template("register.html", form=form)

@users.route("/verify_email/<token>")
def verify_email(token):
    email = confirm_token(token)
    if email:
        user = User.objects(email=email).first()
        user.email_confirmed = True
        user.save()
        flash("Email verified successfully", "success")
    else:
        flash("Email verification failed", "danger")
    return redirect(url_for("users.login"))

@users.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("recipes.index"))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.objects(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            if not user.email_confirmed:
                flash("Please verify your email before logging in", "danger")
                return redirect(url_for("users.login"))
            login_user(user)
            flash("Login successful", "success")
            return redirect(url_for("users.account"))
        else:
            flash("Invalid username or password", "danger")
            return redirect(url_for("users.login"))
    return render_template("login.html", form=form)


# TODO: implement
@users.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("recipes.index"))


@users.route("/account", methods=["GET", "POST"])
@login_required
def account():
    update_username_form = UpdateUsernameForm()
    update_profile_pic_form = UpdateProfilePicForm()
    image = None

    if request.method == "POST":
        if update_username_form.submit_username.data and update_username_form.validate():
            current_user.modify(username=update_username_form.username.data)
            flash("Username updated successfully", "success")
            return redirect(url_for("users.account"))

        if update_profile_pic_form.submit_picture.data and update_profile_pic_form.validate():
            pic_data = update_profile_pic_form.picture.data
            try:
                # Check if there is an existing profile picture
                if current_user.profile_pic:
                    # Replace the existing profile picture
                    current_user.profile_pic.replace(
                        pic_data,
                        content_type=pic_data.content_type
                    )
                else:
                    # Create a new profile picture entry
                    current_user.profile_pic.put(
                        pic_data,
                        content_type=pic_data.content_type
                    )
                current_user.save()
                flash("Profile picture updated successfully", "success")

            except Exception as e:
                flash("There was an error uploading the profile picture.", "danger")
                print(f"Error uploading image: {e}")

            return redirect(url_for("users.account"))
    if current_user.profile_pic:
        image = base64.b64encode(current_user.profile_pic.read()).decode("utf-8")
    return render_template(
        "account.html",
        update_username_form=update_username_form,
        update_profile_pic_form=update_profile_pic_form,
        image=image,
    )

@users.route("/user/<username>")
def user(username):
    user = User.objects(username=username).first()
    if user is None:
        return render_template("404.html", error="User not found")
    # TODO: if we are the user, allow us to delete recipes
    # for now, lets just pass it a list of all recipes that we own
    recipes = Recipe.objects(author=user)
    form = DeleteRecipeForm()
    return render_template("user.html", user=user, recipes=recipes, get_b64_img=get_b64_img, form=form)