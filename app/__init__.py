from flask import Flask, request

#imports the different routes
from app.routes import routes_app

app = Flask(__name__)

#different pages
app.register_blueprint(routes_app)