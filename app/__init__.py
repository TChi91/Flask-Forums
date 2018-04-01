from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

folder_path = os.path.abspath(os.path.dirname(__file__))
#app.config["SQLALCHEMY_DATABASE_URI"] = f"""sqlite:///{os.path.join(folder_path, "my_database.db")}"""
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DATABASE_URL']
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

from app import dummy_data, stores

member_store = stores.MemberStore()
post_store = stores.PostStore()

from app import views
from app import api