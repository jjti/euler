from utils import *

"""
The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of the form;
it contains exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form have been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits:
28433 x 2 ^ 7830457 + 1

Find the last ten digits of this prime number.
"""
t = 1 # total
# for _ in range(0, 7830457):
for _ in range(0, 7830457):
    t *= 2
    t = join(split(t)[-10:])  # last ten digits

print join(split(t * 28433 + 1)[-10:])
