# -*- coding: utf-8 -*-

from expects import *
from fizzbuzzkata import fizzbuzzkata


with describe('FizzBuzz Kata'):
    with context('when execute sayHello'):
        with it('says Hello'):
            result = fizzbuzzkata.say_hello()

            expect(result).to(equal('Hello'))

    with context('Fizz case -> when a number is divisible by 3'):
        with context('when given number is 1'):
            with it('returns the given number 1'):
                a_number = 1

                result = fizzbuzzkata.apply_fizz_to(a_number)

                expect(result).to(1)
