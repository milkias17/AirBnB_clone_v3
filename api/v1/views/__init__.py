#!/usr/bin/python3
"""Module with api view routes"""

from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.index import *