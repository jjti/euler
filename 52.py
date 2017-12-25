import utils

"""
Permuted multiples
Problem 52 
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

def split_map(n):
    """Create a dictionary between an integer and it's digit counts

    ex: split_map(8199) = {'8': 1, '1': 1, '9': 2}
    """
    split_n = utils.split(n)
    MAP = {}
    for m in split_n:
        if m in MAP:
            MAP[m] += 1
        else:
            MAP[m] = 0
    return MAP

def maps_same(m, n):
    """Compare two digit count maps

    return whether the digit counts in the two maps are the same
    """
    for k in n.keys():
        if k not in m or m[k] is not n[k]:
            return False
    return True

ans = -1
i = 1
while ans < 0:
    i += 1
    
    # test 2 - 6 multipliers
    i_m = split_map(i)
    for j in range(2, 7):
        j_m = split_map(i * j)
        if not maps_same(i_m, j_m):
            break
        if j == 6:
            ans = i
print i
