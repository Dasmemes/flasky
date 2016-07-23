from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/kenamu/sqlite3-db/flask1.db'
db = SQLAlchemy(app)
