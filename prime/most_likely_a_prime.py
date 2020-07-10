#!/usr/bin/env python3
"""
Author: David Hull
Date: 7/10/20
Description:
In this module, we use a probable prime test that states the following:

    For a natural number n > 2, if 2^(n-1) ≡ 1 (mod n), then n is very likely prime.

Since this is a probable prime test, we cannot be certain we are finding a prime number unless we use a prime
test such as Wilson's Theorem in the primes.py.However, there is a 99.9999996% chance of finding a prime.

I have yet to see a non-prime number returned. Although, inevitably we will be counting non-primes as primes,
so if you ask for the 100th prime, which is 541, you will instead get 523.

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


#
def nth_prime_probably():
    n = mpmath.mpf(input("What's the Nth prime you want to find? "))

    maybe_a_prime = mpmath.mpf(5)
    number_of_primes_found = 2

    if n > 30000:
        number_of_primes_found = mpmath.ceil(mpmath.fdiv(n, mpmath.ln(n - 1)))

    print(
        f"By the Prime Number Theorem, the {n}th prime is approximately {mpmath.fprod([n, mpmath.ln(n)])}"
    )

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


print()
print(nth_prime_probably())
print("Probably...")
