"""
By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:


Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.
"""


def rectangle_count(x, y):
    """
        the sub_problem. Given a rectangle with dimensions x, y, calc the number of
        rectangles that will fit within it
    """
    contains_count = 0
    # increment thru every possibly sized box and add up all the ways it could fit
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            contains_count += (x / i + x % i) * (y / j + y % j)
    return contains_count


assert rectangle_count(2, 2) == 9
assert rectangle_count(3, 2) == 18


def counting_rectangles(target=2000000, lower_bound=1, upper_bound=2000):
    """
        Notes:
            Another DP problem... harder than last two
            The figure may be helpful, shows how it's fragmenting up the rectangle into larger rectangles
            and counting those

            For every (x, y) combo, find how many rectangles will fit

            Trial and error with upper and lower bounds and the expected area (need to filter on area to run in time)
    """
    # closest is (x, y, rectangle count)
    curr_closest = (0, 0, 0)
    for n in range(lower_bound, upper_bound):
        for m in range(n, upper_bound + 1):
            if n * m > 4000 and n * m < 6500:
                rect_count = rectangle_count(n, m)
                if abs(rect_count - target) < abs(curr_closest[2] - target):
                    curr_closest = (n, m, rect_count)
    return (curr_closest[0] * curr_closest[1], curr_closest)


# outputs 5355 in 12.4 seconds
print counting_rectangles()