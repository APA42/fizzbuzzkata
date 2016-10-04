# -*- coding: utf-8 -*-

import fizzbuzzkata


if __name__ == "__main__":
    for number in range(1, 31):
        print "Input number:", number, "=>", fizzbuzzkata.apply_fizzbuzz_to(number)
