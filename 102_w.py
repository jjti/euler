import math
"""
Three distinct points are plotted at random on a Cartesian plane, for which -1000 <= x, y <= 1000, such that a triangle is formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)

X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.

Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing the co-ordinates of one thousand "random" triangles,
find the number of triangles for which the interior contains the origin.

NOTE: The first two examples in the file represent the triangles in the example given above.
"""


def dist(pt1, pt2=(0, 0)):
    """
        calc the distance between the two tuples (coordinates), using pethag
    """
    return ((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)**0.5


assert dist((0, 2), (0, 4)) == 2.0
assert dist((0, 3), (0, 4)) == 1.0
assert dist((3, 0), (0, 4)) == 5.0


def triangle_containment(test_triangles=None):
    """
        for_each: side of the triangle, form a test triangle between that side and the center as the third point:
            if: the test triangle has a hypotaneus that includes the origin, the origin is not contained
                inside the triangle
    """

    triangles = test_triangles
    if triangles is None:
        triangles = []
        with open("./102.input.txt") as triangle_file:
            for line in triangle_file.readlines():
                pts = [int(pt) for pt in line.strip().split(",")]
                triangles.append([(pts[i], pts[i + 1]) for i in [0, 2, 4]])

    un_contained = 0
    for t in triangles:
        # check if all the distances to from each corner to the other cornders are shorter than
        # the distances from the corner to the origin
        for i, c in enumerate(t):
            edge = dist(c, t[(i + 1) % 3])  # the edge on side of triangle
            # one of the edges from this corner to center
            center_edge_1 = dist(c)
            # other edge from next corner to center
            center_edge_2 = dist(t[(i + 2) % 3])
            if edge < center_edge_1 or edge < center_edge_2:
                un_contained += 1
                break

    return len(triangles) - un_contained


assert triangle_containment([[(-340, 495), (-153, -910), (835, -947)],
                             [(-175, 41), (-421, -714), (574, -645)]]) == 1

# outputs 138 in 0.05 secons
print triangle_containment()