import utils

PRIME_SIEVE = utils.prime_sieve(100000)
PRIME_MUTATED_MAP = {}


def addMutatedPrime(digits, prime):
    """mutate digits within the prime number
    
    randomly drop digits from the prime and add to a "family" of other primes
    with digits dropped in similar locations
    
    from the example, 56003, 56113 and 56333 all share the pattern 56**3
    here, 56**3 should be a key and the value should be the array of values that
    share that signature

    only primes should hit this function
    """
    for i, d in enumerate(digits):
        if d is not "*":
            # replace this index with a wildcard
            newDigits = digits[0:i] + ["*"] + digits[i + 1:]
            newNum = utils.join(newDigits, True)
            if newNum in PRIME_MUTATED_MAP:
                PRIME_MUTATED_MAP[newNum].append(prime)
            else:
                PRIME_MUTATED_MAP[newNum] = [prime]
            addMutatedPrime(newDigits, prime)


def findMutatedPrimeFamily(targetN=5):
    """build up a mutated prime map and return the smallest prime
        that's part of a mutated prime family of the target length
    """
    for prime in PRIME_SIEVE:
        addMutatedPrime(utils.split(prime), prime)

    smallestPrime = None
    for mutatedPrimes in PRIME_MUTATED_MAP.values():
        if len(mutatedPrimes) == targetN:
            if smallestPrime is None or mutatedPrimes[0] < smallestPrime:
                smallestPrime = mutatedPrimes[0]

    return smallestPrime


print(findMutatedPrimeFamily())