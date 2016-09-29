# -*- coding: utf-8 -*-


def say_hello():
    return 'Hello'


def apply_fizz_to(a_number):
    result = a_number % 3
    if result == 0:
        return 'Fizz'
    else:
        return a_number
