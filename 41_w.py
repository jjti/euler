import utils

"""
Pandigital prime
Problem 41 
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

# generate a sieve
SIEVES = utils.prime_sieve(1000000000)

# permute and sort with the greatest numbers first
PERMS = map(lambda x: utils.join(x), utils.permute([1, 2, 3, 4, 5, 6, 7, 8, 9]))
PERMS.sort()
PERMS = [p for p in PERMS[::-1] if p % 2 != 0]
for p in PERMS:
    if SIEVES[p]:
        print p
        break
