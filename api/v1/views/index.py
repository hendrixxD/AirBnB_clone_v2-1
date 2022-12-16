#!/usr/bin/python3

from api.v1.views import app_views
from flask import jsonify

@app.app_views("/status")
def indx():
    return(jsonify{"status":"Ok"})
