import utils


"""
The primes 3, 7, 109, and 673, are quite remarkable.
By taking any two primes and concatenating them in any order the result will always be prime.
For example, taking 7 and 109, both 7109 and 1097 are prime.
The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""


def compare_sets(set1, set2):
    """
        return True if set1 is better than set2, False otherwise
    """
    if len(set1) > len(set2):
        return True
    return len(set1) == len(set2) and sum(set1) < sum(set2)


def best_of_sets(arrs):
    best_set = []
    for a in [r for r in arrs if r]:
        if compare_sets(a, best_set):
            best_set = a
    return best_set


def permute_add(cpls, pairs, current, target):
    """
        params:
            current_req -- the current threshold
    """
    new_arrs = []

    for new_num in pairs:
        test_set = current.union([new_num])

        if len(test_set) == len(current):
            continue
        test_intersection = set.intersection(*[cpls[m] for m in test_set])

        if len(test_intersection) == target and len(test_set) == target:
            new_arrs.append(test_set)
        elif len(test_intersection) >= target:
            #print test_set, new_num, test_intersection
            new_arrs.append(permute_add(cpls, pairs, test_set, target))

    return best_of_sets(new_arrs)


def prime_pair_sets(limit = 800000, key_limit = 670, target_l = 4):
    """
        1. first create all pairings between numbers
        2. then try and find the set with the greatest common value
    """

    P_SET = utils.prime_sieve(limit)
    P_SIEVE = [x for x, p in enumerate(P_SET) if p]

    # cpls = prime couples
    cpls = {p: set([p]) for p in P_SIEVE}
    for p in [p for p in P_SIEVE if p > 10]:
        prime_string = str(p)
        for i in range(1, len(prime_string)):
            f_half = prime_string[:i]
            f_half_int = int(f_half)

            s_half = prime_string[i:]
            if s_half[0] == "0":
                # took way too long to find this
                continue
            s_half_int = int(s_half)

            flipped = int(s_half + f_half)
            if flipped > limit:
                continue

            if P_SET[f_half_int] and P_SET[s_half_int] and P_SET[flipped]:
                cpls[f_half_int].add(s_half_int)
                cpls[s_half_int].add(f_half_int)

    assert permute_add(cpls, cpls[673], set([673]), 4) == set([673, 3, 109, 7])

    best_set = []
    for k in [k for k in sorted(cpls.keys(), reverse = True) if k > key_limit]:
        local_best = permute_add(cpls, cpls[k], set([k]), target_l)
        if compare_sets(local_best, best_set):
            best_set = local_best
    print best_set, sum(best_set)


# prime_pair_sets(10000000, 1000, 5) # 11 sec
prime_pair_sets(10 ** 8, 800, 5) # 119.422 sec
