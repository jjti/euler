"""
We shall define a square lamina to be a square outline with a square "hole" so that the shape possesses vertical and horizontal symmetry.

Given eight tiles it is possible to form a lamina in only one way: 3x3 square with a 1x1 hole in the middle.
However, using thirty-two tiles it is possible to form two distinct laminae.

If t represents the number of tiles used, we shall say that t = 8 is type L(1) and t = 32 is type L(2).
Let N(n) be the number of t ≤ 1000000 such that t is type L(n); for example, N(15) = 832.
What is ∑ N(n) for 1 ≤ n ≤ 10?
"""

limit = 10**6 + 1

L_SIEVE = [0] * (limit + 1)

for rings in [[x for x in range(8, limit, 8)],
              [x for x in range(12, limit, 8)]]:
    for i, r in enumerate(rings):
        sum_here = r
        curr_i = i
        while sum_here < len(L_SIEVE):
            L_SIEVE[sum_here] += 1
            curr_i += 1
            if curr_i < len(rings):
                sum_here += rings[curr_i]
            else:
                break

total = 0
for y in range(1, 11):
    total += len([x for x in L_SIEVE if x == y])

print total  # 1.6 seconds
