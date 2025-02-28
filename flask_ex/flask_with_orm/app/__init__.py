import os

from flask import Flask
from datetime import datetime


app = Flask(__name__, template_folder=os.path.abspath('app/templates'))
from app.base import views
from app.posts import views
from app.comments import views



@app.template_filter('strftime')
def _jinja2_filter_datetime(date, fmt=None):
    if fmt is None:
        fmt = '%Y-%m-%d %H:%M'
    return date.strftime(fmt)