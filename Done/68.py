"""Euler_68

magic gon-rings. find maximum string with smallest outside number first
each row in the ring should some to same number. 

ex: max of a 3-gon-ring is: 4,2,3; 5,3,1; 6,1,2

try making two lists. one for the outer numbers and one for the inner number

take all combinations of 2/3 the input numbers and created inner arrays:
    the inner array can be any permutation of its numbers (with first num appended to end)
        this is precursor to the final list of ring generator
    the outer array can then found among the remaining 1/3, if each triplet adds to 3
"""


def permute(arr):
    """Generate permutations of the array of remaining numbers

    where arr is a list of numbers not included in the existing combinations
    """
    acc = [[]]
    while len(arr) is not 0:
        num_add = arr.pop()  # number to add to every spot in the lists
        acc = [r[0:i] + [num_add] + r[i:] for r in acc for i in range(0, len(r) + 1)]

    # permute on starting index and add on to the last index
    return map(lambda x: x + [x[0]], acc)


def choose(acc, r, count):
    """Choose x number of numbers for the array

    generate a list of all possible choices given count (dec between loops)
    """
    if count is 0:
        return acc

    # generate all permutations as long as some items are left in acc
    perms = [choose(acc + [r[i]], r[i+1:], count - 1)
             for i in range(0, len(r) - count + 1)]

    # flatten results
    if count > 1:
        return [p for e in perms for p in e]
    return perms


def gen_rings(max=6):
    """Generate triplets of rings

    should grab the outer digits first (1/2 of array length), making all combinations of these
    rings are valid of their sum is equivelant
    rings can also be flipped and then reversed
    """
    arr = range(1, max + 1)
    outers = choose([], arr, max / 2)
    rings = []
    s = lambda x,y: x+y
    def ring_gen(x,y,i):
        return [x[i]] + y[i:i+2]
    def rev_rings(x):
        reved = x[::-1]
        return [x[0]] + reved[0:len(x)-1]
    flip = lambda x: [x[0], x[2], x[1]]

    for outer in outers:
        inner_digits = [i for i in arr if i not in outer]

        for inner in permute(inner_digits):
            f = ring_gen(outer, inner, 0)
            a = [f]  # all rows array
            for i in range(1, len(outer)):
                b = ring_gen(outer, inner, i)
                if reduce(s, f) is reduce(s, b):
                    a.append(b)
            if len(a) is len(outer):  # every row was the same
                rings.append(a)
                fl = map(flip, a)
                rings.append(rev_rings(fl))
    for r in rings:
        print r
                
gen_rings(10) #the problem calls for 10
