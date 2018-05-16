"""Utility functions for Project Euler

Some functions are frequently needed like reversing a number or
building up an array of prime numbers
"""

import math
import unittest


def split(n):
    """Split a number into an array of digits

    Ex: split(1029) = [1, 0, 2, 9]
    """
    digits = []
    while n > 0:
        digits.insert(0, n % 10)
        n /= 10
    return digits


def join(n):
    """Join the array of digits in n into a single number

    Ex: join([3, 1, 5, 4]) = 3154
    """
    return reduce(lambda x, y: x * 10 + y, n)


def reverse(n):
    """Reverse the digits of a number

    returns a number with same number of digits, but in reverse order
    ex: reverse(167) = 761
    reverse(190) = 91
    """
    split_array = split(n)
    return join(split_array[::-1])


def palindrome(n):
    """Is a number a palindrome?

    returns whether a number, n, is a palindrome or not
    ex: palindrome(101) = True
    palindrome(10105) = False
    """
    return n == reverse(n)


def choose(n, r):
    """What's N choose R?
    equation is n!/r!(n-r)!

    ex: choose(5, 2) = 10
    choose(5, 1) = 5
    """
    dem = math.factorial(r) * math.factorial(n - r)
    return math.factorial(n) / dem


def prime_sieve(l):
    """Generate a prime number hash up the the limit, l
    1 is not a prime

    based on the sieve of atkin and an example script at:
    https://www.geeksforgeeks.org/sieve-of-atkin/
    """
    # step 1 and 2
    # start of with an all non-prime dictionary
    PRIMES = dict.fromkeys(range(0, l), False)
    for p in [2, 3, 5]:
        PRIMES[p] = True

    # step 3
    lSqr = int(math.floor(math.pow(l, 0.5)))
    for x in range(1, lSqr):
        for y in range(1, lSqr):
            # step 3.1
            n = (4 * x * x) + (y * y)
            if (n <= l and (n % 12 == 1 or n % 12 == 5)):
                PRIMES[n] = True
            # step 3.2
            n = (3 * x * x) + (y * y)
            if (n <= l and n % 12 == 7):
                PRIMES[n] = True
            # step 3.3
            n = (3 * x * x) - (y * y)
            if (x > y and n <= l and n % 12 == 11):
                PRIMES[n] = True

    # step 4
    for x in range(5, lSqr):
        if PRIMES[x]:
            for y in range(x * x, l, x * x):
                PRIMES[n] = False
    return PRIMES


def prime_check(n):
    """Check whether the tested number, n, is a prime number
    """
    for i in range(2, int(math.ceil(math.sqrt(n)))):
        if n % i == 0:
            return False
    return True


def permute(arr):
    """Generate permutations of the array of remaining numbers

    where arr is a list of numbers not included in the existing combinations
    """
    acc = [[]]
    while len(arr) is not 0:
        n = arr.pop()  # number to add to every spot in the lists
        acc = [r[0:i] + [n] + r[i:] for r in acc for i in range(0, len(r) + 1)]
    return acc


def isPandigital(digits):
    """should make all the same digits as a range of 1 to 9"""
    return len(digits) is 9 and len(set(range(1, 10)).difference(
        set(digits))) is 0


class TestStringMethods(unittest.TestCase):
    def test_split(self):
        self.assertEqual(split(109), [1, 0, 9])

    def test_join(self):
        self.assertEqual(join([1, 0, 9]), 109)

    def test_reverse(self):
        self.assertEqual(reverse(601), 106)
        self.assertEqual(reverse(910), 19)

    def test_palindrome(self):
        self.assertEqual(palindrome(601), False)
        self.assertEqual(palindrome(717), True)
        self.assertEqual(palindrome(1010), False)

    def test_factorial(self):
        self.assertEqual(choose(5, 2), 10)

    def test_gen_primes(self):
        self.assertEqual(
            prime_sieve(10), {
                0: False,
                1: False,
                2: True,
                3: True,
                4: False,
                5: True,
                6: False,
                7: True,
                8: False,
                9: False
            })

    def test_isPandigital(self):
        self.assertEqual(isPandigital([1, 2, 3, 4, 6, 5, 8, 7, 9]), True)
        self.assertEqual(isPandigital([1, 2, 3, 4, 6, 5, 8, 9]), False)
        self.assertEqual(isPandigital([1, 2, 3, 4, 6, 5, 8, 8, 9]), False)


if __name__ == '__main__':
    unittest.main()
