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


def digitSlice(n, sliceCount):
    """like split except it only returns a range of the numer
    n {int}                the number to split into an array and subslice
    sliceCount {int}       the slice of digits to get from the number
                            corresponds to n[:sliceCount] (if positive) or
                            n[sliceCount:] (if negative)
    """
    if sliceCount < 0:
        return n % (10**(-sliceCount))
    numDigits = int(math.log10(n) + 1)
    return n / (10**(numDigits - sliceCount))


def join(n, asString=False):
    """Join the array of digits in n into a single number

    n {[int]} the array of integers to turn into a single number
    asString {bool} whether to return as string. useful for keeping 0 at front of number
    Ex: join([3, 1, 5, 4]) = 3154
    """
    if not asString:
        return reduce(lambda x, y: x * 10 + y, n)
    return reduce(lambda x, y: x + y, [str(x) for x in n])


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
    # don't want to return array of digits that start with 0
    return [p for p in acc if p[0] != 0]


def isPandigital(digits, size=9):
    """should include all the digits, 1 to size, inclusive, once"""
    if len(digits) != size: return False
    if size < 10:
        return len(set(range(1, size + 1)).difference(set(digits))) == 0
    return len(set(range(0, size)).difference(set(digits))) == 0


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
        self.assertEqual(isPandigital([1, 3, 2], 3), True)

    def test_splitSlice(self):
        self.assertEqual(splitSlice(12345, -2), [4, 5])
        self.assertEqual(splitSlice(12345, 2), [1, 2])


if __name__ == '__main__':
    unittest.main()
