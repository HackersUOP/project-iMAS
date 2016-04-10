from flask_restful import *
from flask import *


class index(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(
                render_template('index.html'), 200, headers)
