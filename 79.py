from utils import *
"""
A common security method used for online banking is to ask the user for three random characters from a code.
For example, if the code was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

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

319
680
180
690
129
620

319
319680
319680
316980
3162980
3162980

"""

code = []


def sorted_positions(combo):
    """make a list of the character positions in growing password"""
    pos = []
    for c in combo:
        if c in code:
            pos.append(code.index(c))
        else:
            pos.append(len(code))  # insert
            code.append(c)
    pos = sorted(pos)
    for p, c in zip(pos, combo):
        code[p] = c


with open('79.input.txt') as f:
    # cut into a list of 3 letter lists
    allDigits = []
    for line in f:
        allDigits.append(split(int(line)))

    # get the total number count of final password
    for combo in allDigits:
        # get indexes for each digit
        sorted_positions(combo)

#answer is 73162890
print("".join([str(c) for c in code]))
