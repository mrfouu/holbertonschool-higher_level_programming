#!/usr/bin/python3
import json
""" Module that writes an object to a text file using json representation. """
def save_to_json_file(my_obj, filename):
    with open(filename, "w") as f:
        json.dump(my_obj, f)
