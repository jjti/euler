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

print len([x for x in L_SIEVE if x > 0 and x < 11])  # 1.53 seconds
