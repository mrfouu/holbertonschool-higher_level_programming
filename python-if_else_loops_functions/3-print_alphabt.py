#!/usr/bin/python3
for i in range(97, 123):  # Loop from 97 ('a') to 122 ('z')
    if i != 101 and i != 113:  # Exclude 101 ('e') and 113 ('q')
        print(chr(i), end="")  # Print the corresponding character without a newline
