# INPUT: Array of integers
# OUTPUT: Maximum size of contiguous sub array of size k
def maxSum1(arr, k):
    n = len(arr)
    maximum = float('-inf')
    for i in range(0, n-k+1):
        currentSum = 0
        for j in range(k):
            currentSum += arr[i + j]
        maximum = max(currentSum, maximum)
    return maximum


def maxSum2(arr, k):
    n = len(arr)

    if (n < k):
        print("Window larger than array, invalid")
        return

    window_sum = sum([arr[i] for i in range(k)])
    max_sum = window_sum

    for i in range(n-k):
        window_sum = window_sum - arr[i] + arr[i+k]
        max_sum = max(window_sum, max_sum)

    return max_sum


array = [80, -50, 90, 100]
k = 2
print(maxSum2(array, k))
