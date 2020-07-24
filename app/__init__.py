from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

flask_app = Flask(__name__)
flask_app.config.from_object('app.config')

db = SQLAlchemy(flask_app)
ma = Marshmallow(flask_app)

from app.accounts.routes import accounts_bp
from app.users.routes import users_bp

flask_app.register_blueprint(users_bp, url_prefix='/users/')
flask_app.register_blueprint(accounts_bp, url_prefix='/accounts/')

