#!/usr/bin/python3

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route("/status", strict_slashes=False)
def status():
    """
    return the status of application
    """
    return jsonify({"status": "Ok"})


@app_views.route("/stats", strict_slashes=False)
def stats():
    """
    Retrieves count of obects in storage
    """
    from models.amenity import Amenity
    from models.city import City
    from models.place import Place
    from models.review import Review
    from models.state import State
    from models.user import User

    classes = {"amenities": Amenity, "cities": City,
               "Places": Place, "reviews": Review,
               "states": State, "users": User}

    _dict = {}

    for name, cls in classes.items():
        _dict.update({name: storage.count(cls)})

    return jsonify(_dict)
