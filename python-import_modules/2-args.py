#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argc = len(argv)

    if argc == 1:
        print("0 arguments.")
    if argc == 2:
        print("1 argument:")
    if argc > 2:
        print(f"{argc - 1} arguments:")

for x in range(1, argc):
    print("{}: {}".format(x, argv[x]))
