"""
q1
You will be given a list of integers (arr), and a single integer k.
You must create an array of length k from elements of arr such that its unfairness is minimized. 
Call that array - subarr. 
Unfairness of an array is calculated as: max(subarray) - min(subarray)
"""

"""
ex: array [1,4,7,2] k=2
max(1,4) - min(1,4) = 4 - 1 = 3
once calculated all sub arrays then we find that (1,2) => 1

ex: [10,100,200,300,200,1000,20,30], k = 3  => 20.
reason: max(10,20,30) - min(10,20,30) = 30 - 10 = 20

ex: [1,2,3,4,10,20,30,40,100,200], k = 4 => 3
reason: max(1,2,3,4) - min(1,2,3,4) = 4 - 1 = 3

ex: [1,2,1,2,1], k = 2 => 0
reason: max(1,1) - min(1,1) = 0
"""

# Complete the maxMin function below.


def maxMin(k, arr):
    # Return k most proximal values from arr
    # Sort array in ascending order
    # Use sliding window to determine subarray of minimum range

    arr.quickSort()
    # nLogn
    left = 0
    right = k-1
    min_range = float(inf)

    while right < len(arr)-1:
        local_range = arr[right] - arr[left]
        if min_range > local_range:
            min_range = local_range
        left += 1
        right += 1

    return min_range
