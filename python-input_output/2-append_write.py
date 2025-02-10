#!/usr/bin/python3
"""Append to a file."""


def append_write(filename="", text=""):
    """Apprends a string at the end of a text file."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
