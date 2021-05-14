"""
Unique Paths III
On a 2-dimensional grid, there are 4 types of squares:
    1 represents the starting square.  There is exactly one starting square.
    2 represents the ending square.  There is exactly one ending square.
    0 represents empty squares we can walk over.
    -1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square,
that walk over every non-obstacle square exactly once.
Example 1:
    Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
    Output: 2
    Explanation: We have the following two paths:
    1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
    2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
"""
from typing import List


class Solution:

    def __init__(self):
        self.paths = 0

    @staticmethod
    def find_position(grid, rows, cols, element):
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == element:
                    return i, j

    @staticmethod
    def count_zeros(grid, rows, cols):
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    count += 1
        return count

    def backtracking(self, grid, rows, cols, zeros, end, start, new_list):
        x = start[0]
        y = start[1]
        steps = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]
        if len(new_list) == zeros + 1 and (x, y) == end:
            self.paths += 1
            return
        tmp = grid[x][y]
        grid[x][y] = -1
        for x_step, y_step in steps:
            if (-1 < x_step < rows) and (-1 < y_step < cols) and (grid[x_step][y_step] != -1):
                self.backtracking(grid, rows, cols, zeros, end, (x_step, y_step), new_list + [(x_step, y_step)])
        grid[x][y] = tmp

    def unique_paths_iii(self, grid: List[List[int]]) -> int:
        cols, rows = len(grid[0]), len(grid)
        start = self.find_position(grid, rows, cols, 1)
        end = self.find_position(grid, rows, cols, 2)
        zeros = self.count_zeros(grid, rows, cols)
        new_list = []
        self.backtracking(grid, rows, cols, zeros, end, start, new_list)
        return self.paths
