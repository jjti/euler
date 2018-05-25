import utils
import time
"""
Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

65 64 63 62 61 60 59 58 57
66 37 36 35 34 33 32 31 56
67 38 17 16 15 14 13 30 55
68 39 18  5  4  3 12 29 54
69 40 19  6  1  2 11 28 53
70 41 20  7  8  9 10 27 52
71 42 21 22 23 24 25 26 51
72 43 44 45 46 47 48 49 50
73 74 75 76 77 78 79 80 81

1 3 13 31 57
1 5 17 37 65
1 7 21 43 73
1 9 25 49 81

It is interesting to note that the odd squares lie along the bottom right diagonal,
but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime. that is, a ratio of 8/13 = 0.62

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed.
If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
"""
"""
number of digits in each spiral
1, 8, 16, 24
first diagonal number
1, 3, 13, 31, 57    ---    
first digit, increments by 8 each time
2, 10, 18, 26
digits in a spiral arm
0, 2, 4, 6
index
0, 1, 2, 3

(layerIndex + 1) * 4
"""

start = time.time()

spiralIndex, bottomRightCorner, sideLength = 1, 0, 1  # init at zeroeth spiral
primePerc, primeCount, totalCount = 1.0, 0.0, 1.0  # counting middle 1 as first, need float for division
while primePerc >= 0.10:
    sideLength = spiralIndex * 2  # number of digits along one side
    bottomRightCorner = (spiralIndex * 2 + 1)**2

    for x in [bottomRightCorner - i * sideLength for i in range(1, 4)]:
        # check whether they're prime or not using the sieve
        if utils.is_prime(x):
            primeCount += 1

    # find new ratio, will end if < 10%
    totalCount += 4
    primePerc = primeCount / totalCount

    # set the new "last corner"
    spiralIndex += 1

print(primePerc, spiralIndex * 2 - 1, bottomRightCorner)