import utils
"""
70 colored balls are placed in an urn, 10 for each of the seven colors.
What is the expected number of distinct colors in 20 randomly picked balls?
Give your answer with nine digits after the decimal point (a.bcdefghij).
"""


def init():
    """
        create all the permutations for the number drawn from each bucket

        [[10, 10], [10, 9, 1]]...
    """
    acc = [10, 10]


def randomDraw():
    """
        how many ways are there to choose a given count from the 7 buckets
        eg, given that we want to choose 2 colors, how many ways are there

        10 choose 10 == 1, 7 choose 2 == 21, so 21 (1 * 21)
    """
    print utils.choose(7, 3)


# 3 == 0.7 == 2.62404092072 ; 4 == 42
randomDraw()
