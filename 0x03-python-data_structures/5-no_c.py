#!/usr/bin/python3
def no_c(my_string):
    listChar = list(my_string)
    for c in listChar:
        if c == 'c' or c == 'C':
            listChar.remove(c)
    return("".join(listChar))
