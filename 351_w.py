import utils
import time
"""
A hexagonal orchard of order n is a triangular lattice made up of points within a regular hexagon with side n.
The following is an example of a hexagonal orchard of order 5:

Highlighted in green are the points which are hidden from the center by a point closer to it.
It can be seen that for a hexagonal orchard of order 5, 30 points are hidden from the center.

Let H(n) be the number of points hidden from the center in a hexagonal orchard of order n.

H(5) = 30. H(10) = 138. H(1 000) = 1177848.

Find H(100 000 000).
"""


def hex_orchard(order=5):
    t1 = time.time()

    PRIME_FACTORS = utils.gen_prime_factor_map(order + 1)

    CACHE = {}

    def phi(n):
        m = n
        for p in PRIME_FACTORS[m]:
            m -= m / p
        CACHE[n] = m
        return m

    # print(time.time() - t1)

    t2 = time.time()

    length = order
    hidden = 0  # 1 hidden for all but one x = 0 position
    cache = {}
    for x in range(2, length):

        # number of times it fits fully within height available
        y = (length - x / 2)
        folds = y / x
        hidden += (x - phi(x)) * folds

        # count up the remaining coordinates
        left = y % x
        left_set = set()
        for p in PRIME_FACTORS[x]:
            left_set.update(range(p, left + 1, p))
        hidden += len(left_set)

        # fold_text = "folds created: " + str((x - phi(x)) * folds)
        # rem_text = "remainder " + str(left) + " created: " + str(left_hidden)
        # print('{0}, {1}  ->  {2}   {3}'.format(x, y, fold_text, rem_text))

        # nums_hidden = set()
        # for p in PRIME_FACTORS[x]:
        #     nums_hidden.update(range(p, length - x, p))
        # hidden += len(nums_hidden)

    # print(time.time() - t2)

    print hidden * 6

    return 6 * (2 * (order - 1) + 2 * hidden)


# print hex_orchard(5)
# hex_orchard(10)
# hex_orchard(10**4) # 0.48
# hex_orchard(10**5)  # 45.1
hex_orchard(10)
