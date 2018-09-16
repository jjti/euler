# -*- coding: utf-8 -*-

import utils


"""
A Hamming number is a positive number which has no prime factor larger than 5.
So the first few Hamming numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15.
There are 1105 Hamming numbers not exceeding 10**8.

We will call a positive number a generalised Hamming number of type n, if it has no prime factor larger than n.
Hence the Hamming numbers are the generalised Hamming numbers of type 5.

How many generalised Hamming numbers of type 100 are there which don't exceed 109?
"""

def hamming_numbers(limit = 10 ** 9, hamming_cutoff = 100):

    primes = [p for p in utils.prime_sieve(limit, as_list=True) if p > hamming_cutoff and p < limit]
    hammings = [True] * limit
    for n in primes:
        for m in range(n, limit, n):
            hammings[m] = False

    print len([h for h in hammings if h is True])

hamming_numbers()
