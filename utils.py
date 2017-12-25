"""Utility functions for Project Euler

Some functions are frequently needed like reversing a number or
building up an array of prime numbers
"""

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
    rev_array = split_array[::-1]
    return reduce(lambda x,y: x * 10 + y, rev_array)


def palindrome(n):
    """Is a number a palindrome?

    returns whether a number, n, is a palindrome or not
    ex: palindrome(101) = True
    palindrome(10105) = False
    """
    return n == reverse(n)


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
        self.assertEqual(palindrome(101), True)
        self.assertEqual(palindrome(717), True)
        self.assertEqual(palindrome(1010), False)


if __name__ == '__main__':
    unittest.main()
