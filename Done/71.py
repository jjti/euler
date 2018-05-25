def hcf_is_one(num, den):
    """
    return a boolean for whether the highest common denominator between the numerator (num)
    and the denominator (den) is 1
    """
    return den % num != 0


assert hcf_is_one(5, 7) == True
assert hcf_is_one(2, 6) == False


def sorted_fractions(fractions):
    """ sort and return the fractions. the first value in the fraction value """
    return sorted(fractions, lambda x, y: -1 if x[0] - y[0] < 0 else 1)


def ordered_fractions(max_denominator=1000000):
    """
    make list of all reduced proper fractions when the denominator is less than or equal to 1 million
    sort on value
    find the numerator of the fraction immediately to the left of 3/7

    Notes:
        1. can keep numerator very close to something that will produce fractions around 3/7
            keep within some windowed threshold. eg, try to land within 5 of the numerator
            necessary to produce 3/7 with the denominator
    """

    # 3/7 is the key of interest (it's the reference point)
    ref_value = 3.0 / 7

    # a list of tupules with first value as fraction value and second as the numerator
    # will sort on fraction value at the end
    thresh = 2.0 / max_denominator  # thresholding window, want to get within 2
    perc_lower, perc_upper = ref_value - thresh, ref_value + thresh
    fractions = []
    for denominator in range(2, max_denominator + 1):
        # now set the bounds on the numerators range based on what'll produce
        # a number that's close to 3/7
        lower_bound = max([1, int(denominator * perc_lower)])
        upper_bound = min([denominator - 1, int(denominator * perc_upper + 1)])
        for numerator in range(lower_bound, upper_bound):
            # only add to the list if it's a reduced fraction
            if hcf_is_one(numerator, denominator):
                fractions.append((float(numerator) / denominator, numerator))

    print("added " + str(len(fractions)) + " fractions")
    fractions = sorted_fractions(fractions)

    ref_index = None
    for i, frac in enumerate(fractions):
        if frac[0] == ref_value:
            ref_index = i
            break
    return fractions[ref_index - 1][1]


# should return 2. 2/5 is just to the left of 3/7 when d = 8
assert ordered_fractions(8) == 2

print(ordered_fractions())  # output: 428570 in 35 seconds
