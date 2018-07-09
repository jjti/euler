import utils
"""
A hexagonal orchard of order n is a triangular lattice made up of points within a regular hexagon with side n.
The following is an example of a hexagonal orchard of order 5:

Highlighted in green are the points which are hidden from the center by a point closer to it.
It can be seen that for a hexagonal orchard of order 5, 30 points are hidden from the center.

Let H(n) be the number of points hidden from the center in a hexagonal orchard of order n.

H(5) = 30. H(10) = 138. H(1 000) = 1177848.

Find H(100 000 000).
"""


def hex_orchard(length=5):
    total_count = sum(range(1, length + 1))  # num of coordinates

    PRIME_LIST = utils.prime_sieve(total_count, as_list=True)

    hidden = length - 1
    hidden_coors = set()

    for p in PRIME_LIST:
        for x in range(p, length, p):
            for y in range(p, length - x + 1, p):
                hidden_coors.add((x, y))

    return (length - 1 + len(hidden_coors)) * 6


assert sum(range(1, 5 + 1)) == 15
print hex_orchard(5)
print hex_orchard(10)
print hex_orchard(1000)
# assert hex_orchard(1000) == 1177848
print hex_orchard(10**4)
