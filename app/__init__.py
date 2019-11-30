import os
from flask import Flask

root = os.path.dirname(os.path.dirname(__file__))

app = Flask(__name__)
app.config['DEBUG'] = True

from app import routes

