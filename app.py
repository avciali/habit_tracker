import os
from dotenv import load_dotenv
from flask import Flask
from pymongo import MongoClient

from routes import pages

load_dotenv()

def create_app():
    app = Flask(__name__)
    client: MongoClient = MongoClient(os.environ.get("MONGODB_URI"))
    app.db = client.get_default_database()
    app.register_blueprint(pages)

    return app