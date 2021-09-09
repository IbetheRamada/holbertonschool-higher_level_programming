#!/usr/bin/python3
for a in range(ord('a'), ord('z') + 1):
    if (a != 101 and a != 113):
        print("{:c}".format(a), end='')
