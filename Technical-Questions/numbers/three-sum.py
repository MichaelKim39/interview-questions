# INPUT: Array of integers
# OUTPUT: Array of all unique subarrays of size 3 that sum to 0

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        result = []

        for i in range(N):
            # To avoid duplicates, traverse same values at the front
            # i > 0 because otherwise i-1 undefined - still handled later
            if i > 0 & nums[i] == nums[i-1]:
                continue

            # Complement for zero sum is the negative
            target = -1 * nums[i]
            # Define two pointer
            start = i+1
            end = N-1

            while start < end:
                if nums[start] + nums[end] == target:
                    result.append(nums[i], nums[start], nums[end])
                    start += 1

                    # Same logic to avoid duplicates
                    while start < end & nums[start] == nums[start-1]:
                        start += 1
                elif nums[start] + nums[end] < target:
                    start += 1
                else:  # nums[start] + nums[end] > target:
                    end -= 1

        return result
