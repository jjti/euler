import utils


"""
The primes 3, 7, 109, and 673, are quite remarkable.
By taking any two primes and concatenating them in any order the result will always be prime.
For example, taking 7 and 109, both 7109 and 1097 are prime.
The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""


def prime_pair_sets(limit=800000):
    P_SET = utils.prime_sieve(limit)
    P_SIEVE = utils.prime_sieve(limit, as_list=True)

    prime_couples = {p: set([p]) for p in P_SIEVE}
    for p in P_SIEVE:
        prime_string = str(p)
        for i in range(1, len(prime_string)):
            f_half = prime_string[:i]
            f_half_int = int(f_half)

            s_half = prime_string[i:]
            if s_half[0] == '0':
                # took way too long to find this
                continue
            s_half_int = int(s_half)

            flipped = int(s_half + f_half)
            if flipped > limit:
                continue

            if P_SET[f_half_int] and P_SET[s_half_int] and P_SET[flipped]:
                prime_couples[f_half_int].add(s_half_int)
                prime_couples[s_half_int].add(f_half_int)

    print prime_couples[673].intersection(prime_couples[7])
    print prime_couples[673]

    max_set = set(1, 2, 3)
    def max_permute(arr_to_permute):
        """
            however long the current max is, choose that many from the pairs
            try and create all combinations from these, keeping those with at least
            as many total pairs as the max
        """
        for i, n in enumerate(arr_to_permute, 1):
            if prime_couples[n]
        



prime_pair_sets()
