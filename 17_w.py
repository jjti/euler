import utils
"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen)
contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

spellingMap = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}


def tens(n, includeAnd=False):
    """ return the number of letters in the one and tens place """
    n = utils.join(utils.split(n)[-2:])
    numLetterLength = 0
    if n in spellingMap:
        numLetterLength = len(spellingMap[n])  # 0-19
    else:
        numLetterLength = len(
            spellingMap[n / 10 * 10] + spellingMap[n % 10])  # 20-99

    # adding and
    if includeAnd:
        return numLetterLength + 3
    return numLetterLength


def hundreds(n):
    """ return the number of letters in the hundreds place """
    hundreds = utils.split(n)[-3]
    return len(spellingMap[hundreds] + "hundred")


def thousands(n):
    """ return the number of letters in the thousands place """
    thousands = utils.split(n)[-4]
    return len(spellingMap[thousands] + "thousand")


def numberLetterCount(n):
    if n < 100:
        return tens(n)  # never an and
    if n < 1000:
        return hundreds(n) + tens(n, n % 10 != 0)
    return thousands(n) + hundreds(n) + tens(n, n % 10 != 0)


totalLetterCount = sum([numberLetterCount(n) for n in range(1, 1001)])
print([numberLetterCount(n) for n in [342, 115]])
print(totalLetterCount)  # output: 20888
