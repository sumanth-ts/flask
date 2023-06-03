import glob
import importlib
from flask import Flask
from flask_pymongo import PyMongo
from config import MONGO_URI

app = Flask(__name__)
app.config['MONGO_URI'] = MONGO_URI
mongo = PyMongo(app)

# Import your API files
from apis.users_api import users_api
from apis.jile_api import jile_api

# Register the API blueprints
app.register_blueprint(users_api)
app.register_blueprint(jile_api)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
