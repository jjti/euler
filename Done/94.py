import math
"""
It is easily proved that no equilateral triangle exists with integral length sides and integral area.
However, the almost equilateral triangle 5-5-6 has an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose perimeters do not exceed one billion (1,000,000,000).
"""


def pythagoreanTriplets(limits):
    c, m = 0, 2

    # Limiting c would limit
    # all a, b and c
    while c < limits / 3 + 1:

        # Now loop on n from 1 to m-1
        for n in range(1, m):
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n

            if abs(a * 2 - c) < 2:
                if b * (a / 2) % 2 == 0:
                    yield (a * 2, c)

            if abs(b * 2 - c) < 2:
                if a * (b / 2) % 2 == 0:
                    yield (b * 2, c)

            # if c is greater than
            # limit then break it
            if c > limits:
                break

        m = m + 1


def main(limit=100):
    limit += 1
    summed_perims = 0

    for (base, side) in pythagoreanTriplets(limit):
        summed_perims += base + side + side
    return summed_perims


print main(10**9)  # 34 seconds
