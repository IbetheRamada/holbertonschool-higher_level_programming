#!/usr/bin/python3
for i in range (0, 10):
    for a in range (0, 10):
        print("{:d}{:d}".format(i), .format(a), end = '')
        if(i != 9 or a != 9):
            print(", ", end = '')
        