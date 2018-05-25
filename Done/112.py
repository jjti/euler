from utils import split, join


def bouncy_and_increment(n):
    """
        n {int} number to test for bounciness

        return a tuple with a boolean for whether it was bouncy and,
        if it's false, a number for how much to increment the current number by
    """
    digs = split(n)
    # direction can be -1: decreasing, 0: constant, 1: increasing
    direction = 0
    for i, d in enumerate(digs[1:], 1):
        if digs[i - 1] < d:
            # this current digit is greater than last
            if direction == -1:
                # it had been decending
                return (True, 1)
            direction = 1
        elif digs[i - 1] > d:
            # this current digit is less than the last
            if direction == 1:
                # it had been ascending
                return (True, 1)
            direction = -1

    return (False, 1)


assert bouncy_and_increment(10) == (False, 1)
assert bouncy_and_increment(101) == (True, 1)
assert bouncy_and_increment(10123) == (True, 1)
assert bouncy_and_increment(11123) == (False, 1)


def bouncy_numbers(target_ratio=0.99):
    """
    bouncy == not constantly increasing or decreasing

    find the first number at which the ratio of "bouncy" to "non-bouncy"
    numbers reaches, exactly, 99%

    Notes:
        1. should be able to increment thru a large number of digits. The loop should
            be able to self-increment quickly
            ex: at 12000, it's immediately clear that the next 7999 numbers are not-bouncy
            (wound up not needed because it completes in 5 sec)
        2. start at 100, the hint already says the first 99 numbers are not-bouncy
    """
    number, ratio = 1, 0.0  # ratio of bouncy to non-bouncy numbers
    bouncy_numbers = 0.0
    increment = 0  # need this here to subtract from the active number at end of loop

    while ratio < target_ratio:
        bouncy, increment = bouncy_and_increment(number)
        if bouncy:
            bouncy_numbers += 1
        ratio = bouncy_numbers / number
        number += increment

    return number - increment


assert bouncy_numbers(0.9) == 21780
print(bouncy_numbers())  # output: 1587000 in 5.55 seconds
