from flask import Blueprint, jsonify
from flask_pymongo import PyMongo

users_api = Blueprint('users_api', __name__)

@users_api.route('/users', methods=['GET'])
def get_users():
    return("sahfbsf")
