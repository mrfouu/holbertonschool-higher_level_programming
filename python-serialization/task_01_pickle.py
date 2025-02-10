#!/usr/bin/python3
import pickle


class CustomObject:
    """Classe représentant un objet personnalisé."""
    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student


def serialize(self, filename):
    """Function that writes an object to a text file using pickle"""
    import pickle
    try:
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
    except Exception as e:
        print(f"An error occurred while serializing the object: {e}")


@classmethod
def deserialize(cls, filename):
    """Function that reads an object from a text file using pickle"""
    import pickle

    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except Exception as e:
        print(f"An error occurred while deserializing the object: {e}")
        return None
