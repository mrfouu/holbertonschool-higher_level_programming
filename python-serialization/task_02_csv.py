#!/usr/bin/python3
import csv
import json
"""
This module provides functions for serializing and deserializing.
"""


def convert_csv_to_json(csv_filename: str) -> bool:
    """
    Converts a CSV file to a JSON file.
    """
    if not csv_filename.endswith('.csv'):
        raise ValueError("The file must have a .csv extension.")

    try:
        with open(csv_filename, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open("data.json", 'w') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except FileNotFoundError:
        return False
    except (PermissionError, OSError) as e:
        print(f"An error occurred: {e}")
        return False
