from utils import *

"""
A common security method used for online banking is to ask the user for three random characters from a passcode.
For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.
"""

"""
The three digit passcodes in the file are only useful for their relationship to one another.
ie, 735 only says that 7 is before 3 is before 5
or, 129 only says that 1 is before 2 is before 9

For each number, split, try to fit it to the leftmost location possible

First, find the indexes in the existing number where the first is greater than the second is greater than the third
If this does not exist, insert the digit with an unknown position into the list of digits at that missing index
"""

digits = []

with open('Euler_79.test.txt') as f:
    for line in f:
        # split into integers less than 10
        num = split(int(line))

        """The idea is to search for first instance of first number
            if not found, insert at 0 and say it was found at zero
        Then search from the last found index + 1 to end of array for
        the first occurance of second number
            repeat plan if second is not found
        repeat again for third
        """
        inds = 3 * [-1]
        for j in [0,1,2]:
            inds[j] = next((i for i in digits if i == i))


#answer is 1680319
print reduce(lambda x, y: x * 10 + y, digits)
