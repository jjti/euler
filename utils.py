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
    """
    PRIMES = {}
    for i in range(2, l):
        if i not in PRIMES:
            PRIMES[i] = True
            j = i * 2
            while j < l:
                PRIMES[j] = False
                j += i
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
        acc = [r[0:i] + [n] + r[i:]
               for r in acc for i in range(0, len(r)+1)]
    return acc

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
        self.assertEqual(choose(5,2), 10)

    def test_gen_primes(self):
        self.assertEqual(prime_sieve(5), [False, False, False, False, True])


if __name__ == '__main__':
    unittest.main()
