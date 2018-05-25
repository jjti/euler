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
    """calc the distance between the two tuples (coordinates), using pethag
    """
    return ((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)**0.5


assert dist((0, 2), (0, 4)) == 2.0
assert dist((0, 3), (0, 4)) == 1.0
assert dist((3, 0), (0, 4)) == 5.0


def ang(pt1, pt2, pt3):
    """
        find the angle between the 3 points, where the first is the vertex
    """
    p12 = dist(pt1, pt2)
    p13 = dist(pt1, pt3)
    p23 = dist(pt2, pt3)
    return math.acos((p12**2 + p13**2 - p23**2) / (2 * p12 * p13))


def triangle_containment(test_triangles=None):
    """
        find the angle between each corner and the center versus the angle between
        the two corners. If the angle between an edge, the corner and the center is greater than
        the angle between the other two edges, it's not inside the triangle
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
            c1 = t[(i - 1) % 3]
            c2 = c
            c3 = t[(i + 1) % 3]

            corner_to_corner_angle = ang(c2, c1, c3)
            corner_to_origin_angle = ang(c2, c1, (0, 0))

            if corner_to_origin_angle > corner_to_corner_angle:
                un_contained += 1
                break

    return len(triangles) - un_contained


assert triangle_containment([[(-340, 495), (-153, -910), (835, -947)],
                             [(-175, 41), (-421, -714), (574, -645)]]) == 1

# outputs 228 in 0.058 secons
print triangle_containment()