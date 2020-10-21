"""
Do not return anything, modify nums in-place instead.
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        n = len(nums)
        for value in nums:
            if value != 0:
                nums[j] = value
                j += 1
        for i in range(j, n):
            nums[i] = 0
        print(nums)

# O(n) run time
# O(n) space


s = Solution()
s.moveZeroes([0, 2, 0, 1, 4])
