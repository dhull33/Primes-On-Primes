#!/usr/bin/env python3
"""
Author: David Hull
Date: 7/8/20
Description: This module will finds the nth largest prime number using Wilson's Theorem and Converse. Which states that a natural
number n is prime if and only if (n-1)! ≡ -1 (mod n).

Given the nature of factorials, the time it takes to find larger primes increases very quickly. However, it does work
and is very reliable.
"""
import mpmath
import math


def is_prime(n):
    if math.factorial(n - 1) % n == -1 % n:
        return True
    else:
        return False


def definitely_prime():
    n = int(input("What's the Nth prime you want to find? "))

    maybe_a_prime = 5
    number_of_primes_found = 2
    definitely_a_prime = 5

    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        while number_of_primes_found < n:
            if is_prime(maybe_a_prime) == True:
                number_of_primes_found = number_of_primes_found + 1
                definitely_a_prime = maybe_a_prime
            maybe_a_prime = maybe_a_prime + 2

    return definitely_a_prime


print(definitely_prime())
