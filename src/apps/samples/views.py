from flask_restplus import Resource, Api, Namespace
from flask import Blueprint

blueprint = Blueprint('sample', __name__)
api = Api(blueprint, doc='/doc/')

@api.route('/hello')
class Hello(Resource):
    def get(self):
        return 'bwa'
