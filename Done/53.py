import utils

"""
Combinatoric selections
Problem 53
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.
"""
total = 0
for n in range(1, 101):
    for m in range(1, n+1):
        if utils.choose(n, m) > 1000000:
            total += 1
print total

