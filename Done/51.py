import utils
import copy
"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes
among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
"""

PRIMES = utils.prime_sieve(1000000, True)
P_MUTATED_MAP = {}


def insertAtAllLocs(digLocs, digits, prime):
    """Insert the mutated prime into the map as a new set, if it's not already a key,
    or append to the existing set if it is
    """
    for locs in digLocs:
        # all subsets of mutable locations
        mutableNum = copy.copy(digits)
        for l in locs:
            mutableNum[l] = "*"
        mutatedNum = utils.join(mutableNum, True)
        if mutatedNum in P_MUTATED_MAP:
            P_MUTATED_MAP[mutatedNum].add(prime)
        else:
            P_MUTATED_MAP[mutatedNum] = set([prime])


def addMutatedPrime(digits, prime):
    """mutate digits within the prime number
    
    randomly drop digits from the prime and add to a "family" of other primes
    with digits dropped in similar locations
    
    from the example, 56003, 56113 and 56333 all share the pattern 56**3
    here, 56**3 should be a key and the value should be the array of values that
    share that signature

    only primes should hit this function
    """
    digLocs = []  # all the locations of commoon digits
    for n in range(10):
        commonLocs = [i for i, _ in enumerate(digits) if digits[i] == n]
        if len(commonLocs):
            digLocs += [commonLocs] + utils.sub_selections(commonLocs)
    insertAtAllLocs(digLocs, digits, prime)


def findMutatedPrimeFamily(targetN):
    """build up a mutated prime map and return the smallest prime
        that's part of a mutated prime family of the target length
    """
    for prime in PRIMES:
        addMutatedPrime(utils.split(prime), prime)

    smallestPrime, smallestKey = None, None
    for k, primes in P_MUTATED_MAP.items():
        if len(primes) == targetN:
            print(k, min(primes), sorted(primes))
            if smallestPrime is None or min(primes) < smallestPrime:
                smallestPrime, smallestKey = min(primes), k

    return (smallestPrime, smallestKey)


print(findMutatedPrimeFamily(8))