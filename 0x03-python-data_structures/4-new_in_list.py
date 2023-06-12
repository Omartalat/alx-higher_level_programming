#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    listLen = len(my_list) - 1
    if idx < 0 or idx > listLen:
        return (my_list)
    else:
        newList = my_list[:]
        newList[idx] = element
        return (newList)
