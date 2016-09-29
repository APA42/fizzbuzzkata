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

                expect(result).to(equal(1))

        with context('when given number is 2'):
            with it('returns the given number 2'):
                a_number = 2

                result = fizzbuzzkata.apply_fizz_to(a_number)

                expect(result).to(equal(2))

        with context('when given number is 3'):
            with it('returns Fizz'):
                a_number = 3

                result = fizzbuzzkata.apply_fizz_to(a_number)

                expect(result).to(equal('Fizz'))

        with context('when a number is not divisible by 3'):
            with it('returns the same number'):
                a_number = 7

                result = fizzbuzzkata.apply_fizz_to(a_number)

                expect(result).to(equal(a_number))

        with context('when a number is divisible by 3'):
            with it('returns Fizz'):
                a_number = 6

                result = fizzbuzzkata.apply_fizz_to(a_number)

                expect(result).to(equal('Fizz'))
