import utils
import math
"""
The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169;
it turns out that there are only three such loops that exist:

169 -> 363601 -> 1454 -> 169
871 -> 45361 -> 871
872 -> 45362 -> 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 -> 363600 -> 1454 -> 169 -> 363601 (-> 1454)
78 -> 45360 -> 871 -> 45361 (-> 871)
540 -> 145 (-> 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
"""

INT_TO_CHAIN_LENGTH = {}

# little premature optimization here
FACTORIAL = {}
for n in range(0, 10):
    FACTORIAL[n] = math.factorial(n)


def sum_factorial(n):
    """
        split the digits, sum the factorial of each
    """
    return sum([FACTORIAL[m] for m in utils.split(n)])


assert sum_factorial(1) == 1
assert sum_factorial(169) == 363601


def set_chain_length(chain, starting_key):
    """
        given a chain of numbers, cycle thru until there's a repeat
        count up this length and set it for everything, descending
        for the example below, 69 is 5, 363600 is 4, etc

        then do a second loop with just the cyclical numbers
        count up the number of digits in that repeating loop
        set it as the length for everything in the loop

        eg: {69: 363600, 363600: 1454, 1454: 169, 169: 363601, 363601: 1454} == 5
    """

    # first set all lengths from the initial key downward (69 in example)
    chain_length = len(chain)
    linear_chain = set()
    key = starting_key
    while key not in linear_chain:
        INT_TO_CHAIN_LENGTH[key] = chain_length  # set in map
        linear_chain.add(key)  # add to list
        key = chain[key]  # move to next int in list
        chain_length -= 1

    # key now is the first key of the cyclical loop
    # get the length of this loop, and set the length of each in the loop to this length
    loop_length = INT_TO_CHAIN_LENGTH[key]
    loop_key = chain[key]
    while loop_key is not key:
        INT_TO_CHAIN_LENGTH[loop_key] = loop_length
        loop_key = chain[loop_key]


def digit_factorial_chain(upper_limit=1000000, target=60):
    """
        Notes:
            1. Want to store each integer as a reference to the list of repeats that it's associated with
                First map: the key is the integer under study, the value is the key to the other map (any int from the loop/chain) with a list of integers
                Second map: the key is the key from the prior step, the value is the length of the repeating list (no point storing the path)
    """

    for n in range(1, upper_limit):
        orig_n = n
        chain = {}
        chain_list = [n]

        if n in INT_TO_CHAIN_LENGTH:
            continue

        while True:
            # sum the factorial of each digit
            new_n = sum_factorial(n)

            if new_n in chain:
                chain[n] = new_n  # add this to chain now
                # we've already seen this number in this chain
                # increment through the chain, counting up the non-repeating portion, the loop
                set_chain_length(chain, orig_n)
                break
            elif new_n in INT_TO_CHAIN_LENGTH:
                # we've seen this digit in another chain
                # get its length (existing_num_length, and add backwards to set everything
                # in the chain_list. No need to use set_chain_length
                existing_num_length = INT_TO_CHAIN_LENGTH[new_n]
                for i, num in enumerate(chain_list):
                    INT_TO_CHAIN_LENGTH[
                        num] = (len(chain_list) - i) + existing_num_length
                break

            # set the link from this number to the next
            chain[n] = new_n
            chain_list.append(new_n)
            n = new_n

    # count up the number of chains with a length of 60
    assert INT_TO_CHAIN_LENGTH[69] == 5
    assert INT_TO_CHAIN_LENGTH[540] == 2
    assert INT_TO_CHAIN_LENGTH[45360] == 3

    return len([
        INT_TO_CHAIN_LENGTH[n] for n in range(1, upper_limit)
        if INT_TO_CHAIN_LENGTH[n] >= target
    ])


# outputs 402 in 5 seconds
print(digit_factorial_chain())