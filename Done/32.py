import utils
from sets import Set
"""
Pandigital products
Problem 32 
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

7245 is unusual, 39 x 186 = 7254, multiplicand, multiplier and product is 1 thru 9 pandigital
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

PRODUCTS = Set()
PANS = utils.permute(range(1, 10))
for p in PANS:
    for c in range(1, 6):  # multiplicand
        for d in range(c + 1, 7):  # product
            multiplicand = utils.join(p[0:c])
            multiplier = utils.join(p[c:d])
            product = utils.join(p[d:])
            if multiplicand * multiplier == product:
                PRODUCTS.add(product)
print reduce(lambda x, y: x + y, PRODUCTS)
