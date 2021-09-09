#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    lastn = number % -10
else:
    lastn = number % 10

if (lastn > 5):
    print('Last digit of {} ' .format(number), 'is {} an is greater than 5'.format(lastn))
elif (lastn == 0):
    print('Last digit of {} ' .format(number), 'is {} and is zero' .format(lastn))
elif (lastn < 5):
        print('Last digit of {} ' .format(number), 'is {} and is less than 6 and not 0' .format(lastn))