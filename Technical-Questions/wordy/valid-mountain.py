class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        n = len(A)
        i = 1

        if n < 3:
            return False

        while i < n and A[i] > A[i-1]:
            i += 1

        # Because either array is not increasing or only increasing
        if i == 1 or i == n:
            return False

        while i < n and A[i] < A[i-1]:
            i += 1

        return i == n

# Time complexity = O(N)
# Space complexity = O(1) because only requires 2 variables
