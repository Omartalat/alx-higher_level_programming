#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    n = []
    for number in my_list:
        if (number % 2) == 0:
            n.append(True)
        else:
            n.append(False)
    return(n)
