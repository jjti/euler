# -*- coding: utf-8 -*-

import math

import utils


"""
A positive integer n is called squarefree, if no square of a prime divides n, thus 1, 2, 3, 5, 6, 7, 10, 11 are squarefree, but not 4, 8, 9, 12.

How many squarefree numbers are there below 250?
"""

# 11, 21
def squarefree_approach_1(limit=2 ** 50):
    
    upper_bound = int(math.floor(math.sqrt(limit)))

    primes = utils.prime_sieve(upper_bound, as_list=True)

    squares = set()
    for p in primes:
        sqr = p ** 2
        for q in xrange(sqr, limit / 2, sqr):
            squares.add(q)

    return len(squares)

def squarefree_approach_2(limit = 2 ** 50):
    upper_bound = int(math.floor(math.sqrt(limit)))

    # start at the top prime
    primes = utils.prime_sieve(upper_bound, as_list=True)
    primes = sorted(primes, reverse=True)
    primes_sqrd = [p ** 2 for p in primes]

    # divide the limit by the number of times this fits within in it
    print len(primes_sqrd)
    prev_counts = {}
    non_squares = 0
    for (i, p) in enumerate(primes_sqrd):
        count = int(math.floor(limit / p)) + 1
        count -= sum([int(math.floor(prev_p / p)) for prev_p in primes_sqrd[:i]])
        non_squares += count
        prev_counts[p] = count
    return limit - non_squares


print squarefree_approach_2()
