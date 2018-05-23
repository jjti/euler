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


def digit_slice(n, sliceCount):
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


def join(n, as_string=False):
    """Join the array of digits in n into a single number

    n {[int]} the array of integers to turn into a single number
    asString {bool} whether to return as string. useful for keeping 0 at front of number
    Ex: join([3, 1, 5, 4]) = 3154
    """
    if not as_string:
        return reduce(lambda x, y: x * 10 + y, n)
    return "".join([str(x) for x in n])


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


def prime_sieve(limit, as_list=False):
    """Generate a prime number hash up the the limit, l
    1 is not a prime

    as_list returns just the list of primes beneath that limit

    based on the sieve of atkin and an example script at:
    https://www.geeksforgeeks.org/sieve-of-atkin/
    """
    assert limit > 3
    sieve_list = [False] * (limit + 1)
    sieve_list[2:4] = (True, True)

    # Part I: preliminary work
    x = x_squared = 1
    while x_squared < limit:
        y = y_squared = 1
        while y_squared < limit:
            n = 4 * x_squared + y_squared
            if n <= limit and n % 12 in (1, 5):
                sieve_list[n] = not sieve_list[n]

            n = 3 * x_squared + y_squared
            if n <= limit and n % 12 == 7:
                sieve_list[n] = not sieve_list[n]

            if x > y:
                n = 3 * x_squared - y_squared
                if n <= limit and n % 12 == 11:
                    sieve_list[n] = not sieve_list[n]
            y += 1
            y_squared = y * y
        x += 1
        x_squared = x * x

    # Part II: Remove the squares of primes (and their multiples)
    r = 5
    r_squared = r * r
    while r_squared < limit:
        if sieve_list[r]:
            for n in range(r_squared, len(sieve_list), r_squared):
                sieve_list[n] = False
        r += 1
        r_squared = r * r

    # Part III: Append everything into a list
    if as_list:
        return [x for x, p in enumerate(sieve_list) if p]
    return dict.fromkeys([x for x, p in enumerate(sieve_list) if p], True)


def is_prime(n):
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


def sub_selections(arr):
    """Create an array of arrays for all possible sub selections
    add the results to the accumulator list

    eg: [1, 2, 3] = [[1, 2], [1, 3], [2, 3], [1], [2], [3]]
    """
    acc = {}

    def subslice(subArr):
        if len(subArr) < 2: return
        for i in range(len(subArr)):
            subSelect = subArr[0:i] + subArr[i + 1:]
            acc[join(subSelect, True)] = subSelect
            subslice(subSelect)

    subslice(arr)
    return acc.values()


def is_pandigital(digits, size=9):
    """should include all the digits, 1 to size, inclusive, once"""
    if len(digits) != size: return False
    if size < 10:
        return len(set(range(1, size + 1)).difference(set(digits))) == 0
    return len(set(range(0, size)).difference(set(digits))) == 0


def factorize(num, prime_list, prime_set):
    """
        return a list of prime factors for the number
        a prime_list is needed (from a prior sieve or something)
    """
    factors = set()

    for prime in prime_list:
        if num in prime_set:
            factors.add(num)
            return factors
        elif num == 0 or prime > num:
            return factors
        elif num % prime == 0:
            factors.add(prime)
            num /= prime


def gen_factor_map(limit=1000000):
    """
        like the sieve or erathanous, but am making a list of factors at each index
    """
    factors = dict.fromkeys(range(2, limit + 1), None)
    for n in range(2, limit / 2 + 1):
        if factors[n] == None:
            for m in range(n * 2, limit, n):
                if factors[m] == None:
                    factors[m] = [n]
                else:
                    factors[m].append(n)
    return factors


assert factorize(4998, prime_sieve(1000, True),
                 set(prime_sieve(1000, True))) == set([2, 3, 7, 17])
assert factorize(10, prime_sieve(1000, True),
                 set(prime_sieve(1000, True))) == set([2, 5])


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
        sieve = prime_sieve(100)
        for prime in [3, 5, 7, 11, 13, 17]:
            self.assertTrue(sieve[prime])

    def test_is_pandigital(self):
        self.assertEqual(is_pandigital([1, 2, 3, 4, 6, 5, 8, 7, 9]), True)
        self.assertEqual(is_pandigital([1, 2, 3, 4, 6, 5, 8, 9]), False)
        self.assertEqual(is_pandigital([1, 2, 3, 4, 6, 5, 8, 8, 9]), False)
        self.assertEqual(is_pandigital([1, 3, 2], 3), True)

    def test_splitSlice(self):
        self.assertEqual(digit_slice(12345, -2), 45)
        self.assertEqual(digit_slice(12345, 2), 12)

    def test_sub_selections(self):
        subselects = sub_selections([1, 2, 3])
        for s in [[1], [2], [3], [1, 2], [1, 3], [2, 3]]:
            self.assertTrue(s in subselects)

        subselects = sub_selections([0, 1, 2, 4])
        for s in [[0, 1, 2], [0, 1, 4], [1, 2, 4]]:
            self.assertTrue(s in subselects)


if __name__ == '__main__':
    unittest.main()
