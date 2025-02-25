from flask import Flask


app = Flask(__name__)
from app.base import views