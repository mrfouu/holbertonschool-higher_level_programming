#!/usr/bin/python3
""" Module that writes an object to a text file using json representation. """
import json


def load_from_json_file(filename):
    """writes an object to a text file using json representation."""
    with open(filename) as f:
        return json.load(f)
