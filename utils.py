"""Utility functions for Project Euler

Some functions are frequently needed like reversing a number or
building up an array of prime numbers
"""

import unittest

def reverse(n):
    """Reverse the digits of a number

    returns a number with same number of digits, but in reverse order
    ex: reverse(167) = 761
    reverse(190) = 91
    """
    new = 0
    while n > 0:
        new *= 10
        new += n % 10
        n /= 10
    return new


def palindrome(n):
    """Is a number a palindrome?

    returns whether a number, n, is a palindrome or not
    ex: palindrome(101) = True
    palindrome(10105) = False
    """
    return n == reverse(n)


class TestStringMethods(unittest.TestCase):

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
