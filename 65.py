import utils
"""
The square root of 2 can be written as an infinite continued fraction.
The infinite continued fraction can be written, 2**0.5 = [1;(2)], (2) indicates that 2 repeats ad infinitum. In a similar way, 23**0.5 = [4;(1,3,1,8)].

It turns out that the sequence of partial values of continued fractions for square roots provide the best rational approximations.
Let us consider the convergents for 2**0.5.
 
Hence the sequence of the first ten convergents for 2**0.5 are:

1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...


What is most surprising is that the important mathematical constant,
e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

The first ten terms in the sequence of convergents for e are:

2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.
"""


def denom_seq(length=30):
    """
		What is most surprising is that the important mathematical constant,
		e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

		make that seq ^
	"""
    return [2 * (i / 3) if not i % 3 else 1 for i in range(2, length + 2)]


assert denom_seq(9) == [1, 2, 1, 1, 4, 1, 1, 6, 1]


def convergence_of_e(upper_limit=100):
    """
		increment the fraction until we reach upper limit
		sum the digits in the numerator after incrementing target number of times

		Notes:
			1. the multiplier here (in the denom_seq above), is like a multiplier
				for the numerator and denominator when calculating the next fraction
			2. if p, q is the next numerator and denominator, and we have
				a, b and c, d as the n-1 and n fractions:
				p = a + multiplier(c)
				q = b + multiplier(d)
			3. aannndddd the denominator has nothing to do with it...
	"""
    # a and b are last and current numerators
    a, b = 2, 3
    for multiplier in denom_seq(upper_limit - 1)[1:]:
        a, b = b, a + multiplier * b
    return sum(utils.split(b))


assert convergence_of_e(10) == 17
# outputs 272 in 0.05 seconds
print convergence_of_e(100)
