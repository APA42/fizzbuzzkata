# -*- coding: utf-8 -*-

from expects import *
from fizzbuzzkata import fizzbuzzkata


with describe('FizzBuzz Kata'):
    with context('when execute sayHello'):
        with it('says Hello'):
            result = fizzbuzzkata.say_hello()

            expect(result).to(equal('Hello'))