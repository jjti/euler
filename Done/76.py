import utils
import copy
"""
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

csum(4) + csum(3) * csum(2)
csum(4) => 4
csum(3) => 2
csum(2) => 1

5, 1 => 1
4, 2 => 6
3 => 1

csum(6) == 10
csum(5) + csum(4) * csum(2) + csum(3)
csum(5) => 6
csum(4) => 4
csum(2) => 1
csum(3) => 2

How many different ways can one hundred be written as a sum of at least two positive integers?
"""


def counting_summations(target=100):
    """
        create the starting pairs for the number, and try to add up all the combos
    """
    ways = dict.fromkeys(range(0, target + 1), 0)
    ways[0] = 1

    for i in range(1, target):
        for j in range(i, target + 1):
            ways[j] += ways[j - i]
    print(ways)
    print(ways[target])


counting_summations(100)
"""
4 ['1111', '112', '13', '22']
5 ['11111', '1112', '113', '122', '14', '23']
5 ['41', '32', '311', '221', '2111', '11111']
6 ['111111', '11112', '1113', '1122', '114', '123', '15', '222', '24', '33']
7 ['1111111', '111112', '11113', '1114', '25', '1222', '16',  '1123', '34', '115', '11122', '124', '133', '223']
"""


def orig_implementation(num):
    """
        append fragmented digits to acc

        for every number list for last int:
            1. add 1 to its start, add each to new list
            2. for every digit in the number
                2.1 if it's smaller than the digit after it, or if there's no digit after it,
                    increment the digit by one and new number combo to new list
    """
    curr_n, combos = 2, [[1, 1]]

    while curr_n < num:
        curr_n += 1
        new_combos = {utils.join([1] * curr_n, True): [1] * curr_n}

        for c in combos:
            new_combos[utils.join([1] + c, True)] = [1] + c

            # 2 increment first if it's not bigger than the one after it
            if c[0] < c[1]:
                inc_first_digit = [c[0] + 1] + c[1:]
                new_combos[utils.join(inc_first_digit, True)] = inc_first_digit

            # 3. increment last digit
            inc_last_digit = c[:-1] + [c[-1] + 1]
            new_combos[utils.join(inc_last_digit, True)] = inc_last_digit
        combos = new_combos.values()
    return set([tuple(c) for c in combos])


# print([utils.join(i, True) for i in orig_implementation(7)])
# 50 in 19 seconds
# 60 in 25 seconds
# print orig_implementation(12).difference(counting_summations(12))