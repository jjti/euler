import utils
"""
The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053).
In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""


def genCubicMap(l=10000):
    """
        1. create all cubes up a trillion
        2. split cube into digits, sort, store in map as:
            [sortedDigits]: list(cube)
            add additional cubes to that list, will later be used to
            count up to the target numberof permutated primes
    """
    cubicMap = {}
    for x in range(2, l):
        cube = x**3

        # digit signature for this cube
        digits = utils.join(sorted(utils.split(cube)), True)
        if digits in cubicMap:
            # other cubes are already indexed here
            cubicMap[digits].append(cube)
        else:
            cubicMap[digits] = [cube]
    return cubicMap


def permuatedCubes(n=5):
    """look thru the map of cube values for digit signatures with n number of cubes
    should return 41063625 for a cubic count, n, of 3 """
    smallestCube = None
    digitToCubeListMap = genCubicMap()
    for cubes in digitToCubeListMap.values():
        if len(cubes) == n:
            print(cubes)
            # cubes are naturally sorted on input, cubes[0] is the smallest
            if smallestCube is None or cubes[0] < smallestCube:
                smallestCube = cubes[0]
    return smallestCube


print(permuatedCubes())  # outputs 127035954683
