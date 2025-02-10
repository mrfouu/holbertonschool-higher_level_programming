#!/usr/bin/python3
import json
""" Module that writes an object to a text file using json representation. """
def load_from_json_file(filename):
    with open(filename) as f:
        return json.load(f)
