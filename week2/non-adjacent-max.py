from typing import list
# https://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/#:~:text=Max%20sum%20excluding%20the%20current,max%20of%20incl%20and%20excl.

# INPUT - array of integers
# OUTPUT - sum of largest sub-array of non-adjacent elements

# EXAMPLE - [-2, 1, 3, -4, 5]
# Method to get subarrays of non-adjacent elements efficiently
# Method to compare sum of subarrays efficiently


def nonAdjacentMax(nums: List(int)) -> str:
    include = nums[0]
    exclude = 0

    for value in nums:
        new_exclude = max(exclude, include)

        include = exclude + value
        exclude = new_exclude

    return max(exclude, include)
