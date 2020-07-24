from flask import request, jsonify

class User:

    def index(self):
        return 'index'

    def fetch_one(self):
        if request.method == 'GET':
            return jsonify({'find_by_id': request.args.get('id')})
        
    def storage(self):
        return 'storage'
    
    def restore(self, id):
        return 'restore'
    
    def delete(self, id):
        return 'delete'