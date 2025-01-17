#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argc = len(argv)
    result = 0
    for x in range(1, argc):
        result += int(argv[x])
    print(result)
