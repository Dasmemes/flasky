from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/kenamu/sqlite3-db/flask1.db'
app.config['SECRET_KEY'] = '6qnWQf4AaB7VTFg0qHr/An+iDE8ZeVWNmVepGZMa9yz8PPWF8LNJHmUcV5YOkzCB'
db = SQLAlchemy(app)

login_manger = LoginManager()
login_manger.init_app(app)
flask_bcrypt = Bcrypt(app)

from application.users import models as user_models
from application.users.views import Users
app.register_blueprint(Users, url_prefix='/users')


@login_manger.user_loader
def load_user(user_id):
    return user_models.User.query.get(int(user_id))


@app.route('/', methods=["GET"])
def home():
    return render_template('index.html')