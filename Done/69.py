import utils
"""
Euler's Totient function, q(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n.
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, q(9)=6.

It can be seen that n=6 produces a maximum n/q(n) for n <= 10.

Find the value of n <= 1,000,000 for which n/q(n) is a maximum.
"""

PRIME_LIST = utils.prime_sieve(1000000, as_list=True)
FACTOR_MAP = utils.gen_factor_map()


def phi(k):
    """
        return the number of relative primes
        number of ints, n, from 1 <= n_i <= k, where GCD(i, n) == 1
    """
    """
        Misc notes used in dev:
        3 % 3 -> 3 - 1

        4 % 2 -> 2. 4 - 2

        10 % 2 -> 5. 10 - 5
        5 % 5 -> 5 - 1

        30 / 2 -> 15. 30 - 15
        15 / 3 -> 5. 15 - 5
        10 / 5 -> 1. 10 - 2

        20 % 2 -> 10. 20 -> 10
        10 % 5 -> 2. 10 -> 8
    """
    if FACTOR_MAP[k]:
        for p in FACTOR_MAP[k]:
            k -= k / p
        return k
    return k - 1


assert phi(20) == 8
assert phi(30) == 8
assert phi(60) == 16
assert [phi(n) for n in range(2, 11)] == [1, 2, 2, 4, 2, 6, 4, 6, 4]
assert phi(783678) == 218592


def totient_maximum(limit=10):
    """
        find the number with the maximum number/relative primes ratio
        up to the provided limit

        Notes:
            1. Won't be an odd number
            2. Probably going to be divisible by 60
    """
    max_ratio, max_n = 0.0, 0

    # start_and_inc = 60 if limit > 100 else 2
    for num in range(2, limit + 1, 2):
        relative_ratio = float(num) / phi(num)
        if relative_ratio > max_ratio:
            max_ratio, max_n = relative_ratio, num
    return max_n, max_ratio


assert totient_maximum() == (6, 3.0)
# output: 510510 in 5.5 seconds
print(totient_maximum(1000000))
