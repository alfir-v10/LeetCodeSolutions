"""
Subrectangle Queries
Implement the class SubrectangleQueries which receives a rows x cols rectangle as
a matrix of integers in the constructor and supports two methods:
1. updateSubrectangle(int row1, int col1, int row2, int col2, int newValue)
    Updates all values with newValue in the subrectangle whose upper left coordinate is (row1,col1) and bottom right coordinate is (row2,col2).
2. getValue(int row, int col)
    Returns the current value of the coordinate (row,col) from the rectangle.
"""
from typing import List


class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle

    def update_subrectangle(self, row1: int, col1: int, row2: int, col2: int, new_value: int) -> None:
        for row in range(row1, row2 + 1):
            for col in range(col1, col2 + 1):
                self.rectangle[row][col] = new_value

    def get_value(self, row: int, col: int) -> int:
        return self.rectangle[row][col]
