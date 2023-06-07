#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 1:
        x = i - 32
    else:
        x = i
    print("{}".format(chr(x)), end="")
       
