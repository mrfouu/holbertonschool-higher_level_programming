#!/usr/bin/python3
def new_in_list(list, idx, liste):
    if idx < 0:
        return list
    elif idx >= len(list):
        return list
    else:
        my_list = list[:]
        my_list[idx] = liste
        return my_list
