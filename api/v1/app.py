#!/usr/bin/python3
"""Module that runs api routes"""

from os import getenv

from flask import Flask

from api.v1.views import app_views
from models import storage

app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_storage(e):
    storage.close()


if __name__ == "__main__":
    HOST = getenv("HBNB_API_HOST") or "0.0.0.0"
    PORT = int(getenv("HBNB_API_PORT")) or 5000
    app.run(HOST, PORT, threaded=True)