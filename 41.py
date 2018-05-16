import utils
"""
Pandigital prime
Problem 41 
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

# permute and sort with the largest numbers first
for i in range(9, 0, -1):
    PERMS = [utils.join(x) for x in utils.permute(range(1, i))]
    PERMS = sorted(PERMS, reverse=True)
    for p in PERMS:
        if utils.prime_check(p):
            print(p)
            raise StopIteration
