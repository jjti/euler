import utils
"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn-1 + Fn-2, where F1 is 1 and F2 is 1
It turns out that F541, which contains 113 digits, is the first Fibonacci number for which the last nine digits are 1-9 pandigital 
(contain all the digits 1 to 9, but not necessarily in order). And F2749, which contains 575 digits, is the first Fibonacci number
for which the first nine digits are 1-9 pandigital.

Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find k.
"""

digits = range(1, 10)
pandigitals = set([utils.join(n) for n in utils.permute(range(1, 10))])


def firstAndLastTenPandigital(n):
    """return whether the first and last ten digits are pandigital"""
    if utils.digit_slice(n, -9) in pandigitals:
        if utils.digit_slice(n, 9) in pandigitals:
            return True
    return False


last, curr, index = 1, 1, 2
while True:
    last, curr, index = curr, last + curr, index + 1  # fib increment
    if index > 100 and firstAndLastTenPandigital(curr):
        print(index)  # output: 329468 in 23 seconds
        break