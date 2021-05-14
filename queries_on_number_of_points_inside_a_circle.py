"""
Queries on Number of Points Inside a Circle
You are given an array points where points[i] = [x_i, y_i] is the coordinates of the ith point on a 2D plane.
Multiple points can have the same coordinates.
You are also given an array queries where queries[j] = [x_j, y_j, r_j] describes a circle centered at (x_j, y_j)
with a radius of r_j.
For each query queries[j], compute the number of points inside the j-th circle.
Points on the border of the circle are considered inside.
Return an array answer, where answer[j] is the answer to the j-th query.
"""
from typing import List


class Solution:
    @staticmethod
    def count_points(points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answer = []
        for querie in queries:
            count_points = 0
            for point in points:
                if pow(point[0] - querie[0], 2) + pow(point[1] - querie[1], 2) <= pow(querie[2], 2):
                    count_points += 1
            answer.append(count_points)
        return answer
