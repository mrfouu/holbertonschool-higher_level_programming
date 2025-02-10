#!/usr/bin/python3

"""Defines function."""


def read_file(filename=""):
    """Prints contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
