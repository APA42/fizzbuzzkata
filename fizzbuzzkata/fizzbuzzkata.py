# -*- coding: utf-8 -*-


def say_hello():
    return 'Hello'


def apply_fizzbuzz_to(a_number):
    if (a_number % 3) == 0:
        return 'Fizz'
    elif (a_number % 5) == 0:
        return 'Buzz'
    else:
        return a_number
