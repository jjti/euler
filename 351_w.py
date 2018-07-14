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


def hex_orchard(o=5):
    t1 = time.time()

    PRIME_FACTORS = utils.gen_prime_factor_map(o + 1)

    def phi(n):
        for p in PRIME_FACTORS[n]:
            n -= n / p
        return n

    t2 = time.time()

    print(time.time() - t1)

    ans = sum([n - phi(n) for n in range(1, o + 1)]) * 6

    print(time.time() - t2)

    return ans

    # hidden = [[False] * (o + 1) for _ in range(o + 1)]
    # for x in range(1, o + 1):
    #     for y in range(0, o - x + 1):
    #         new_x = x + x
    #         new_y = y + y
    #         while new_x <= o and new_y <= o:
    #             hidden[new_x][new_y] = True
    #             new_x += x
    #             new_y += y

    # # number of times it fits fully within height available
    # y = length - x
    # folds = y / x
    # hidden += (x - phi(x)) * folds

    # # count up the remaining coordinates
    # left = y % x
    # left_set = set()
    # for p in PRIME_FACTORS[x]:
    #     left_set.update(range(p, left + 1, p))
    # hidden += len(left_set)

    # print o
    # for x in range(o + 1):
    #     for y in range(o + 1):
    #         if hidden[x][y] and x + y == o:
    #             print(x, y)

    # return len([c for row in hidden for c in row if not c])


# for n in range(1, 15):
#     hex_orchard(n)
# assert hex_orchard(5) == 30  # 30
# assert hex_orchard(10) == 138  # 138
# assert hex_orchard(1000) == 1177848  # 1177848
print hex_orchard(10**6 * 5)
