from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)

folder_path = os.path.abspath(os.path.dirname(__file__))
#app.config["SQLALCHEMY_DATABASE_URI"] = f"""sqlite:///{os.path.join(folder_path, "my_database.db")}"""
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://fbkopuwxkdozco:75abe2c71cf8e243dbb6aa98c8a83179cfde7f01a51dff52e0bb8560b857dd16@ec2-54-235-109-37.compute-1.amazonaws.com:5432/d7baun45bp7drk"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

from app import dummy_data, stores

member_store = stores.MemberStore()
post_store = stores.PostStore()

#dummy_data.seed_stores(member_store, post_store)

from app import views
from app import api
