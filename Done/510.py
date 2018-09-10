import math


def valid_c(a, b, c):
    return abs((a * b) / float(a + b) - c) < 0.000000001


def circleTangents(limit):
    """
    (6.25, 2.777777) 1 [(225, 100, 36)]
    (16.0, 1.777777) 1 [(144, 16, 9)]
    (9.0, 2.25) 5 [(36, 9, 4), (108, 27, 12), (72, 18, 8), (180, 45, 20), (144, 36, 16)]
    (4.0, 4.0) 50 [(4, 4, 1), (76, 76, 19), (20, 20, 5), (92, 92, 23), (36, 36, 9), (40, 40, 10), (176, 176, 44), (124, 124, 31), (196, 196, 49), (12, 12, 3)]
    """

    # z (x + y) = xy
    # z = (xy) / (x + y)
    upper = int(math.sqrt(limit)) + 1
    triples = set()
    for b in range(1, upper):
        for a in range(b, upper):
            c = (a * b) / float(a + b)
            if c % 1 < 0.00000001:
                triples.add((a**2, b**2, int(c)**2))

    final = set()
    for (a, b, c) in triples:
        for m in range(1, limit / a + 1):
            if a * m <= limit:
                final.add((a * m, b * m, c * m))

    total = 0
    for (a, b, c) in final:
        total += a + b + c
    print total


# 100 in 0.172
# 100 == 3072
# 200 == 12379
# 300 == 28282
# 10**4 == 31418891 in 0.05 secs
# 10**5 == 3148756421 in 0.09 secs
# 10**6 == 315177355539 in 0.84 secs
# 10**7 == 31526709841370 in 6.5 secs
circleTangents(10**9)
