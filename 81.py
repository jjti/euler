def path_sum_two_ways(test_matrix=None):
    """
    read in the input file, and find the sum of the minimum path
    from the top left position to the top right position

    Notes:
        1. Looks like a dynamic programming problem. Ie, start bottom
        right and find the sum of the minimum path from the current square
        to the bottom right
    """
    matrix = test_matrix
    if test_matrix is None:
        # import the downloaded matrix
        matrix = []
        with open("81.input.txt") as matrix_file:
            for line in matrix_file:
                matrix.append([int(num) for num in line.split(",")])

    # initialize distances at None
    min_path = [[None] * len(matrix)] * len(matrix)
    max_ind = len(matrix) - 1  # it's a square matrix
    for i in range(max_ind, -1, -1):  # vertical
        for j in range(max_ind, -1, -1):  # horizontal
            if i == max_ind and j == max_ind:
                # we're in the bottom right corner
                min_path[i][j] = matrix[i][j]
            elif j == max_ind and i < max_ind:
                # we're along the right side of the matrix
                # have to go down
                min_path[i][j] = matrix[i][j] + min_path[i + 1][j]
            elif j < max_ind and i == max_ind:
                # we're along the bottom of the matrix
                # have to go right
                min_path[i][j] = matrix[i][j] + min_path[i][j + 1]
            else:
                # we're not up against either side of the matrix
                # find the minimum route from this to the right or downwards
                min_path[i][j] = matrix[i][j] + min(
                    [min_path[i + 1][j], min_path[i][j + 1]])
    return min_path[0][0]


assert path_sum_two_ways([[131, 673, 234, 103, 18], [201, 96, 342, 965, 150],
                          [630, 803, 746, 422, 111], [537, 699, 497, 121, 956],
                          [805, 732, 524, 37, 331]]) == 2427
print(path_sum_two_ways())  # output: 427337 in 0.056 seconds
