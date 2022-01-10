from flask.views import MethodView
from flask import jsonify

class ApiController(MethodView):
    def get(self):
        return jsonify({
            "message": "Hello World!"
        }), 200