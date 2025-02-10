#!/usr/bin/python3
import csv
import json


def convert_csv_to_json(csv_filename):
    """Function that writes an object to a text file using csv"""
    with open(csv_filename, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)
        return json.dumps(data)

    """Function that reads an object from a text file using json"""
    with open(json_filename, 'w') as file:
        json.dump(data, file)
        print(f"Data  serialized and saved to '{json_filename}'")

    with open(json_filename, 'r') as file:
        data = json.load(file)
        return data
