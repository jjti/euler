# -*- coding: utf-8 -*-

import math
import resource

from bitarray import bitarray

import utils

resource.setrlimit(resource.RLIMIT_DATA, (10000000 * 1024, 10000000 * 1024))


"""
A positive integer n is called squarefree, if no square of a prime divides n, thus 1, 2, 3, 5, 6, 7, 10, 11 are squarefree, but not 4, 8, 9, 12.

How many squarefree numbers are there below 250?
"""

# 11, 21
def squarefree(limit=2 ** 50):
    
    upper_bound = int(math.floor(math.sqrt(limit)))

    primes = utils.prime_sieve(upper_bound, as_list=True)

    squares = set()
    for p in primes:
        sqr = p ** 2
        for q in xrange(sqr, limit / 2, sqr):
            squares.add(q)

    return len(squares)


print squarefree()
