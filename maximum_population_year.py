"""
You are given a 2D integer array logs where each logs[i] = [birthi, deathi]
indicates the birth and death years of the ith person.
The population of some year x is the number of people alive during that year.
The ith person is counted in year x's population if x is in the inclusive range [birthi, deathi - 1].
Note that the person is not counted in the year that they die.
Return the earliest year with the maximum population.

Example 1:
    Input: logs = [[1993,1999],[2000,2010]]
    Output: 1993
    Explanation: The maximum population is 1, and 1993 is the earliest year with this population.
Example 2:
    Input: logs = [[1950,1961],[1960,1971],[1970,1981]]
    Output: 1960
    Explanation:
        The maximum population is 2, and it had happened in years 1960 and 1970.
        The earlier year between them is 1960.
"""

from typing import List
import numpy as np


class Solution:

    @staticmethod
    def maximum_population(logs: List[List[int]]) -> int:
        min_year, max_year = logs[0]
        for i in range(len(logs)):
            min_year, max_year = min(min_year, logs[i][0]), max(max_year, logs[i][1])
        population = [0] * (max_year - min_year)
        for pair in logs:
            for i in range(pair[0], pair[1]):
                population[i - min_year] += 1
        return population.index(max(population)) + min_year

    @staticmethod
    def maximum_population_np(logs: List[List[int]]) -> int:
        logs_np = np.array(logs)
        min_year = logs_np.min()
        population = np.zeros(logs_np.max() - min_year)
        for pair in logs:
            pair_range = np.arange(pair[0], pair[1]) - min_year
            population[pair_range] += 1
        return population.argmax() + min_year

