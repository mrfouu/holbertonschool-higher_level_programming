#!/usr/bin/python3
"""
This module provides functions for serializing and deserializing.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Function that writes an object to a text file using xml
    """
    root = ET.Element("dictionary")
    for key, value in dictionary.items():
        entry = ET.SubElement(root, key)
        entry.text = str(value)
        root.append(entry)
    tree = ET.ElementTree(root)

    with open(filename, "wb") as file:
        tree.write(file)
    print(f"Data  serialized and saved to '{filename}'")


def deserialize_from_xml(filename):
    """
    Function that reads an object from a text file using xml
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    dictionary = {}
    for entry in root:
        key = entry.tag
        value = entry.text
        dictionary[key] = value
    return dictionary
