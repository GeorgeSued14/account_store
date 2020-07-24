from flask import Blueprint
from app.accounts.views import Account

accounts_bp = Blueprint('accounts_bp', __name__)

accounts_bp.add_url_rule('/', view_func=Account.index, methods=['GET'])
accounts_bp.add_url_rule('/<id>', view_func=Account.find_by_id, methods=['GET'])
accounts_bp.add_url_rule('/new/', view_func=Account.storage, methods=['POST','GET'])
accounts_bp.add_url_rule('/restore/<id>', view_func=Account.restore, methods=['PUT','POST'])
accounts_bp.add_url_rule('/delete/<id>', view_func=Account.delete, methods=['DELETE'])

