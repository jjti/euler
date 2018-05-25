import utils
"""
It is possible to show that the square root of two can be expressed as an infinite continued fraction.

2 ** 1/2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408,
but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?
"""


def SquareOfTwoGenerator(limit=1000):
    """
    numerators = 3, 7, 17, 41, 99
    denominators = 2, 5, 12, 29, 70

    the next numerator is the current numerator + 2 times the last denominator
    the next denominator is the sum of the current numerator and denominator
    """
    index, num, den = 0, 3, 2
    while index < limit:
        """set the next numerator and denominator
        return whether the numerator has more digits than the denominator (see above)"""
        hit = len(utils.split(num)) > len(utils.split(den))
        num, den = num + 2 * den, num + den
        index += 1
        yield hit


# now run thru the iterator and accumulate all the hits
count = 0
for numerBiggerThanDenom in SquareOfTwoGenerator():
    if numerBiggerThanDenom:
        count += 1

print(count)
