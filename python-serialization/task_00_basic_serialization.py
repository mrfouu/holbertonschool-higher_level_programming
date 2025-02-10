#!/usr/bin/python3
import json
""" Module that writes an object to a text file using json"""


def serialize_and_save_to_file(data, filename):
    """ Function that writes an object to a text file using json"""
    with open(filename, 'w') as file:
        json.dump(data, file)
        print(f"Data  serialized and saved to '{filename}'")


def load_and_deserialize(filename):
    """ Function that reads an object from a text file using json"""
    with open(filename, 'r') as file:
        data = json.load(file)
        return data
