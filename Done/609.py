# -*- coding: utf-8 -*-

import utils


"""
For every n≥1 the prime-counting function π(n) is equal to the number of primes not exceeding n.
E.g. π(6)=3 and π(100)=25.

We say that a sequence of integers u=(u0,⋯,um) is a π sequence if

un≥1 for every n
un+1=π(un)
u has two or more elements
For u0=10 there are three distinct π sequences: (10,4), (10,4,2) and (10,4,2,1).

Let c(u) be the number of elements of u that are not prime.
Let p(n,k) be the number of π sequences u for which u0≤n and c(u)=k.
Let P(n) be the product of all p(n,k) that are larger than 0.
You are given: P(10)=3×8×9×3=648 and P(100)=31038676032.

Find P(108). Give your answer modulo 1000000007.
"""


class node:
    def __init__(self, value, comp, parent):
        self.value = value
        self.comp = comp
        self.parent = parent
        self.cs = []  # c values for all chains from this node upwards

        compInc = 0
        if comp:
            compInc += 1

        if parent is not None:
            parentComp = compInc
            if parent.comp:
                parentComp += 1
            self.cs = [c + compInc for c in parent.cs] + [parentComp]


def prime_counting(target):
    target += 1
    primes = utils.prime_sieve(target + 1)

    pi_counts = [0] * (target + 1)
    primes_seen = 0
    for n in range(target + 1):
        if primes[n]:
            primes_seen += 1
        pi_counts[n] = primes_seen

    ks = [0] * (target + 1)
    nodes = {}
    last_pi = None
    last_node = None
    last_prime = False
    cut_off = pi_counts[target]
    for n in range(target):
        pi = pi_counts[n]
        if pi == last_pi and not last_prime:
            for c in last_node.cs:
                ks[c] += 1
            nodes[n] = last_node
            continue

        # if pi > cut_off:
        #     continue

        parent = None
        comp = True
        if pi > 0:
            parent = nodes[pi]
            comp = not primes[n]

        new_node = node(n, comp, parent)
        # print n, new_node.cs
        for c in new_node.cs:
            ks[c] += 1

        nodes[n] = new_node
        last_node = new_node
        last_pi = pi
        last_prime = primes[n]

    def P(n):
        """ Let P(n) be the product of all p(n,k) that are larger than 0. """
        ps = []
        for i, count in enumerate(ks):
            if count > 0:
                # print i, count
                ps.append(count)
        return reduce(lambda x, y: x * y, ps)

    return P(target - 1)


# print prime_counting(10)
assert prime_counting(100) == 31038676032
# print prime_counting(10 ** 7) % 1000000007  # 742870469 in 20 sec
print prime_counting(10 ** 8) % 1000000007  # 172023848 in 20 sec
