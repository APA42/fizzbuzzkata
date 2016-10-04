# -*- coding: utf-8 -*-

from expects import *
from fizzbuzzkata import fizzbuzzkata


LIST_NUMBERS_NOT_DIVISIBLE_BY_3 = [1, 2, 4, 5, 7, 8]
LIST_NUMBERS_DIVISIBLE_BY_3 = [3, 6, 9]


with describe('FizzBuzz Kata'):
    with context('when execute sayHello'):
        with it('says Hello'):
            result = fizzbuzzkata.say_hello()

            expect(result).to(equal('Hello'))

    with context('Fizz case'):
        with context('when a number is not divisible by 3'):
            with it('returns the same number'):
                for a_number in LIST_NUMBERS_NOT_DIVISIBLE_BY_3:
                    result = fizzbuzzkata.apply_fizzbuzz_to(a_number)

                    expect(result).to(equal(a_number))

        with context('when a number is divisible by 3'):
            with it('returns Fizz'):
                for a_number in LIST_NUMBERS_DIVISIBLE_BY_3:
                    result = fizzbuzzkata.apply_fizzbuzz_to(a_number)

                    expect(result).to(equal('Fizz'))
