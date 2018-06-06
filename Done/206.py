"""
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each "_" is a single digit.
"""


def incrementingSquare():
    """
    Notes:
    
    1. only numbers ending in **70 can produce a square with a 9 in
    the hundreds place. Can start at 70 + sqrt of the target number and
    increment by 100

    2. can write out a string for the target number, and increment thru both it
    and the newly squared number, testing at each index
    """
    target = "1234567890"

    for n in range(70 + 10**9, 2 * 10**9, 100):
        digs = str(n**2)
        if all([digs[i * 2] == c for i, c in enumerate(target)]):
            return (n, digs)


# output: (1389019170, "1929374254627488900") in 9 secs
print(incrementingSquare())
