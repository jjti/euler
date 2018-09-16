# -*- coding: utf-8 -*-

from operator import mul

import utils


"""
The radical of n, rad(n), is the product of the distinct prime factors of n. For example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.

If we calculate rad(n) for 1 ≤ n ≤ 10, then sort them on rad(n), and sorting on n if the radical values are equal, we get:

Let E(k) be the kth element in the sorted n column; for example, E(4) = 8 and E(6) = 9.

If rad(n) is sorted for 1 ≤ n ≤ 100000, find E(10000).
"""

def ordered_radicals(limit = 100000, target = 10000):
    factor_map = utils.gen_prime_factor_map(limit+1)

    rad_arr = []
    for (n, facts) in sorted(factor_map.items(), key=lambda tup: tup[0]):
        rad_arr.append((n, reduce(mul, facts, 1)))
    
    rad_arr.sort(key=lambda tup: tup[1])
    print rad_arr
    #print rad_arr
    print rad_arr[target + 1]
    return rad_arr[target+1][0]
    


assert ordered_radicals(10, 4) == 8
assert ordered_radicals(10, 6) == 9

ordered_radicals(100000, 10000) # 21417 in 0.296 seconds
