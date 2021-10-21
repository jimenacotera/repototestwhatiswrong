"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""
from http import HTTPStatus
from flask import Flask
from flask_restx import Resource, Api


app = Flask(__name__)
api = Api(app)

HELLO = 'Hola'
WORLD = 'mundo'


@api.route('/hello')
class HelloWorld(Resource):
    """
    The purpose of the HelloWorld class is to have a simple test to see if the
    app is working at all.
    """
    def get(self):
        """
        A trivial endpoint to see if the server is running.
        It just answers with "hello world."
        """
        return {HELLO : WORLD} 


@api.route('/list_rooms') 
class ListRoom(Resource):
    """
    This endpoints returns a list of rooms
    """
    def get(self):
        """
        returns a list of chat rooms
        """
        return {"Software Engineering": {"num_users": 17} , "AI": {"num_users": 27}, }


@api.route('/endpoints')
class Endpoints(Resource):
    """
    This class will serve as live, fetchable documentation of what endpoints
    are available in the system.
    """
    def get(self):
        """
        The `get()` method will return a list of available endpoints.
        """
        endpoints = sorted(rule.rule for rule in api.app.url_map.iter_rules())
        return {"Available endpoints": endpoints}


@api.route('/create_user/<username>')
class CreateUser(Resource):
    """
    This class supports fetching a list of all pets.
    """
    @api.response(HTTPStatus.OK, 'Success')
    def post(self, username):
        """
        This method returns all pets.
        """
        return username
