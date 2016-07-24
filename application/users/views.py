from flask import Blueprint, flash, render_template, url_for, redirect
from flask_login import login_user, logout_user, current_user

from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length

from .models import User
from application import flask_bcrypt


Users = Blueprint('users', __name__, template_folder='templates')


class LoginForm(Form):

    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(), Length(min=6)])


@Users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('users.account'))

    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(username=form.username.data).first()

        if not user:
            flash("No such user exists.")
            return render_template('users/login.html', form=form)

        if not(flask_bcrypt.check_password_hash(user.password, form.password.data)):
            flash("Invalid password.")
            return render_template('users/login.html', form=form)

        login_user(user, remember=True)
        flash("Success! You are now logged in.")
        return redirect(url_for('users.account'))

    return render_template('users/login.html', form=form)


@Users.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect('/')


@Users.route('/account', methods=['GET'])
def account():
    return render_template('users/account.html')