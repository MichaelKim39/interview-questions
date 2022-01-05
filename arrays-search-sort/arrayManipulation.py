# LDBOWIT
"""
Inputs: Array size n, 2D Operations Array
Output: Maximum value of array after operations provided
Details: Indices are inclusive and are 1-indexed. IE a 1 represents the first element not 0

EXAMPLE:
n = 10
queries = 
a b k
1 5 3
4 8 7
6 9 1
Array after each operation =
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[3, 3, 3, 3, 3, 0, 0, 0, 0, 0]
[3, 3, 3, 10, 10, 7, 7, 7, 0, 0]
[3, 3, 3, 10, 10, 8, 8, 8, 1, 0]
"""

# BRUTE FORCE
# O(operations * n)
# Optimisation - simply alter left and right indices to be value and -value (Calculate running sum instead)


def arrayManipulation(n, queries):
    nums = [0] * n
    for i in queries:
        leftIndex = queries[i][0] - 1
        rightIndex = queries[i][1] - 1
        value = queries[i][2]
        addValue(nums, value, leftIndex, rightIndex)
    return max(nums)


def addValue(nums, value, leftIndex, rightIndex):
    for i in range(leftIndex, rightIndex+1):
        nums[i] += value
