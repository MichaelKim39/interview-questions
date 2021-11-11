from typing import List

"""
TWO SUM
Input: Array of integers
Output: Indices of the two elements that add to target value
Conditions: Exactly one solution exists, may not use same element twice
Example: [2,7,11,15], target 9 -> [0,1]
"""

# Brute force
# Time complexity = O(n^2)
# Space complexity = O(1)


def brute_two_sum(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    for i in range(n+1):
        for j in range(i+1, n+1):  # Only need to check values from i onwards
            if (i != j) & (nums[i] + nums[j] == target):
                return [i, j]
    raise Exception("No solution found")


# 1 Pass optimal variant
# Hashmap lookup and insert takes O(1)
# Time complexity = O(n) iterations costing O(1) each
# Space complexity = Stores at most O(n) elements
def optimal_two_sum(nums: List[int], target: int) -> List[int]:
    # Define hashMap to map integers to indices
    # integer : index
    numsMap = dict()

    for index, value in enumerate(nums):
        complement = target - value
        if complement in numsMap:
            return [numsMap[complement], index]
        numsMap[value] = index
    raise Exception("No solution found")


def main():
    print("Main")
    nums = [2, 7, 11, 15]
    print(optimal_two_sum(nums, 9))


if __name__ == '__main__':
    main()
