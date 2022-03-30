#!/usr/bin/env python3
import sys


def odd_generator(some_num):
    for odd_number in range(1, some_num + 1, 2):
        yield odd_number


for number in odd_generator(15):
    print(number)
