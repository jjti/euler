import utils
"""
Pandigital multiples
Problem 38

Take the number 192 and multiply it by each of 1, 2, and 3:

192 x 1 = 192
192 x 2 = 384
192 x 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645,
which is the concatenated product of 9 and (1,2,3,4,5).

9 x 1 = 9
9 x 2 = 18
9 x 3 = 27
9 x 4 = 36
9 x 5 = 45

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""
"""Steps for brute force

every number needs to be tested until an array of digits has been built up that's pandigital []bool
at first sign of it being pandigital, concatenate and compare the summed values

hints:
has to be greater than 918273645

"""


def testableInts():
    """generator for all the probable integers. must start with 9"""
    yield 9
    for n in range(91, 99):
        yield n
    for n in range(912, 988):
        yield n
    for n in range(9123, 9877):
        yield n
    for n in range(91234, 98766):
        yield n


maxNum = 0
for x in testableInts():
    num, i = [], 1
    while len(num) < 9:
        num = num + utils.split(x * i)
        i += 1
    if utils.isPandigital(num):
        maxNum = max([utils.join(num), maxNum])
print(maxNum)
