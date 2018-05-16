"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""


def monthToDayCount(i, year):
    """Given a months index and the year, return the number of days in that month

    i {int} the index of the month
    year {int} the current year
    """
    # jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec
    if i in [0, 2, 4, 6, 7, 9, 11]:
        # jan, march, may, july, august, oct, dec
        return 31
    elif i in [3, 5, 8, 10]:
        # apr, jun, sep, nov
        return 30
    elif i == 1:
        # sep
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            # it's a leap year
            return 29
        return 28
    else:
        raise RuntimeError("Invalid month")


def sundayCount():
    """Start counting Sundays
    """

    sundayCount = 0

    # Jan 1 1900 was a Monday
    dayOfWeek = 1  # 0-6, 0 = Sunday

    # run up until 21 century
    for year in range(1900, 2001):
        for month in range(0, 12):
            for _ in range(0, monthToDayCount(month, year)):
                dayOfWeek += 1
                dayOfWeek %= 7
                if (dayOfWeek == 0 and year > 1900):
                    sundayCount += 1

    return sundayCount


print(sundayCount())  # output: 5218
