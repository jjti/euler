import utils
import time
"""
Consider the divisors of 30: 1,2,3,5,6,10,15,30.
It can be seen that for every divisor d of 30, d+30/d is prime.

Find the sum of all positive integers n not exceeding 100 000 000
such that for every divisor d of n, d+n/d is prime.
"""


def prime_generating_integers(upper_limit=1000):
    """
        Notes:
            1. Only even integers. Any odd integer + 1 won't be prime
            2. Relatedly, can filter on only number one less than a prime, since
                the num divided by itself == 1, so n+1 needs to be prime
            3. Add one to the sum
    """
    start = time.time()
    PRIME_LIST = utils.prime_sieve(upper_limit, True)
    PRIMES = set(PRIME_LIST)

    print(time.time() - start)
    start = time.time()

    ANS = set([p - 1 for p in PRIME_LIST if 2 + p / 2 in PRIMES])
    for i, p in enumerate(PRIME_LIST):
        for n in range(p, upper_limit, p):
            if n in ANS:
                while n % p == 0:
                    if p + n / p not in PRIMES:
                        ANS.discard(n)
                        break
                    p *= PRIME_LIST[i]
                p = PRIME_LIST[i]
            if n in ANS:
                while n % p == 0:
                    if p + n / p not in PRIMES:
                        ANS.discard(n)
                        break
                    p += PRIME_LIST[i]

    print(time.time() - start)
    start = time.time()

    assert all(
        [n in ANS for n in [2, 6, 30, 42, 58, 78, 210, 310, 330, 382, 462]])
    assert all([n not in ANS for n in [8, 12, 26, 32, 36, 270, 378]])

    return sum(ANS) + 1  # also include 1...


"""
2 [1, 2]
6 [1, 2, 3, 6]
10 [1, 2, 5, 10]
22 [1, 2, 11, 22]
30 [1, 2, 3, 5, 6, 10, 15, 30]
42 [1, 2, 3, 6, 7, 14, 21, 42]
58 [1, 2, 29, 58]
70 [1, 2, 5, 7, 10, 14, 35, 70]
78 [1, 2, 3, 6, 13, 26, 39, 78]
82 [1, 2, 41, 82]
102 [1, 2, 3, 6, 17, 34, 51, 102]
130 [1, 2, 5, 10, 13, 26, 65, 130]
190 [1, 2, 5, 10, 19, 38, 95, 190]
210 [1, 2, 3, 5, 6, 7, 10, 14, 15, 21, 30, 35, 42, 70, 105, 210]
310 [1, 2, 5, 10, 31, 62, 155, 310]
330 [1, 2, 3, 5, 6, 10, 11, 15, 22, 30, 33, 55, 66, 110, 165, 330]
358 [1, 2, 179, 358]
382 [1, 2, 191, 382]
"""

print prime_generating_integers(100000000)