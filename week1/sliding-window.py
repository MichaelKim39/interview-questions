"""
LARGEST SUBSEQUENCE
Input: Array of integers, size of subsequences to consider
Output: Subsequence with greatest sum of specified size
"""

# Window size k


def slidingWindowMax(nums, k):
    n = len(nums)
    max_sum = float("-inf")

    for left_index in range(n-k+1):
        # Calculate sum
        window_sum = 0
        for j in range(left_index, left_index + k):
            window_sum += nums[j]
        print(left_index, ' : ', window_sum)
        # update maximum
        max_sum = max(window_sum, max_sum)

    return max_sum


def main():
    # Driver code
    arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
    k = 4
    print(slidingWindowMax(arr, k))


if __name__ == '__main__':
    main()
