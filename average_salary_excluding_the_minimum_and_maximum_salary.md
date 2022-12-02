[Average Salary Excluding the Minimum and Maximum Salary](https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary)
```Python
    class Solution:
    def average(self, salary: List[int]) -> float:
        min_salary = min(salary)
        max_salary = max(salary)
        len_salary = len(salary)
        total_salary = sum(salary)
        if min_salary != max_salary:
            return (total_salary - min_salary - max_salary) / (len_salary - 2)
        return (total_salary - min_salary) / (len_salary - 1) 
         
```