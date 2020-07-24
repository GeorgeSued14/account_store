from flask import Blueprint
from app.users.views import User

user = User()

users_bp = Blueprint('users_bp', __name__)

users_bp.add_url_rule('/', view_func=user.index, methods=['GET'])
users_bp.add_url_rule('/usr/', view_func=user.fetch_one, methods=['GET'])
users_bp.add_url_rule('/new/', view_func=user.storage, methods=['POST','GET'])
users_bp.add_url_rule('/restore/<id>', view_func=user.restore, methods=['PUT','POST'])
users_bp.add_url_rule('/delete/<id>', view_func=user.delete, methods=['DELETE'])

