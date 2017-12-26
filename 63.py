import utils

"""Powerful digit counts
Problem 63 
The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""
count = 0
for i in range(1, 100): # base
    for j in range(1, 100): # power
        if len(utils.split(i ** j)) == j:
            count += 1
print count
