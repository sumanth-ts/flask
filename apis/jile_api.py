from flask import Blueprint, jsonify
from flask_pymongo import PyMongo

jile_api = Blueprint('jile_api', __name__)

@jile_api.route('/jile', methods=['GET'])
def get_users():
    return("jile")
