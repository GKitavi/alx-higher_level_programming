#!/usr/bin/python3
import random
n = random.randint(-10000, 10000)
if n < 0:
    last_digit = ((n * -1) % 10) * -1
else:
    last_digit = n % 10
if last_digit > 5:
    print("Last digit of {} is {} and is greater than 5".format(n, last_digit))
elif last_digit == 0:
    print("Last digit of {} is {} and is 0".format(n, last_digit))
elif last_digit < 6 and last_digit != 0:
    print("Last digit of {} is {} and is less\
 than 6 and not 0".format(n, last_digit))
