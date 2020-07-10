#!/usr/bin/env python3
"""
Author: David Hull
Date: 7/10/20
Description: Something really dope.
"""

import mpmath
import math


def probably_prime(an_integer):
    n = mpmath.mpf(an_integer)
    two = mpmath.mpf(2)
    one = mpmath.mpf(1)
    power = mpmath.power(two, n - one)

    if mpmath.fmod(power, n) == mpmath.fmod(one, n):
        return True
    else:
        return False


def nth_prime_probably():
    n = mpmath.mpf(input("What's the Nth prime you want to find? "))

    maybe_a_prime = mpmath.mpf(5)
    number_of_primes_found = mpmath.floor(mpmath.fdiv(n, mpmath.ln(n)))

    definitely_a_prime = mpmath.mpf(5)

    if n == 1:
        return 2
    elif n == 2:
        return 3
    elif n == 3:
        return 5
    else:
        while number_of_primes_found < n:
            if probably_prime(maybe_a_prime) == True:
                number_of_primes_found = number_of_primes_found + 1
                definitely_a_prime = maybe_a_prime
            maybe_a_prime = maybe_a_prime + mpmath.mpf(2)

    return definitely_a_prime


print(nth_prime_probably())
print("Probably...")