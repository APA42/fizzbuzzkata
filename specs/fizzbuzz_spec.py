# -*- coding: utf-8 -*-

from expects import *
from fizzbuzzkata import fizzbuzzkata


LIST_NUMBERS_NOT_DIVISIBLE_BY_3 = [1, 2, 4, 7, 8]
LIST_NUMBERS_DIVISIBLE_BY_3 = [3, 6, 9]
LIST_NUMBERS_NOT_DIVISIBLE_BY_5 = [1, 2, 4, 7, 8]
LIST_NUMBERS_DIVISIBLE_BY_5 = [5, 20]
LIST_NUMBERS_DIVISIBLE_BY_5_AND_BY_3 = [15, 30]


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

    with context('Buzz case'):
        with context('when a number is not divisible by 5'):
            with it('returns the same number'):
                for a_number in LIST_NUMBERS_NOT_DIVISIBLE_BY_5:
                    result = fizzbuzzkata.apply_fizzbuzz_to(a_number)

                    expect(result).to(equal(a_number))

        with context('when a number is divisible by 5'):
            with it('returns Buzz'):
                for a_number in LIST_NUMBERS_DIVISIBLE_BY_5:
                    result = fizzbuzzkata.apply_fizzbuzz_to(a_number)

                    expect(result).to(equal('Buzz'))

    with context('FizzBuzz case'):
        with context('when a number is divisible by 5 and by 3'):
            with it('returns FizzBuzz'):
                for a_number in LIST_NUMBERS_DIVISIBLE_BY_5_AND_BY_3:
                    result = fizzbuzzkata.apply_fizzbuzz_to(a_number)

                    expect(result).to(equal('FizzBuzz'))

        with context('when a number is not divisible by 5 and by 3'):
            with it('returns the same number'):
                for a_number in LIST_NUMBERS_DIVISIBLE_BY_5 + LIST_NUMBERS_NOT_DIVISIBLE_BY_3:
                    result = fizzbuzzkata.apply_fizzbuzz_to(a_number)

                    expect(result).not_to(equal('FizzBuzz'))
