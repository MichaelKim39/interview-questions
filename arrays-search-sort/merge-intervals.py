"""
LCEBOWIT

IN - Array of intervals [start, end]
OUT - Array of merged intervals covering input intervals

Questions
    Are intervals in order
    Is array sorted
    What qualifies as an overlap
    Think of edge cases immediately

Brute force - 
    Traverse array
    Compare i with i+1
    if mergeable
        merge
        restart traversal from 0th interval
    otherwise continue traversal

Compares in worst case every interval with every other
O(n^2) to check mergeable
Merging just requires taking range of both arrays of size 2, which is linear, but must be done at most logn times
O(n^2 + logn)

BUD
    Bottleneck - having to compare so many times
    Unused - nothing unused
    Duplicate - don't think so

Optimised -
    Sort intervals - basically quicksort but run twice so O(2nlogn)
    Then compare as usual, but only one walkthrogh required
    Now only O(n) checks & O(n) merges
    overall O(nlogn)

Example - 
    i = 0
    [1,3] [3,4] [4,5]
    [1,4] [3,4] [4,5]
    [1,4] [4,5]
    i = 1
    [1,5] [4,5]
    []
    
"""

from typing import List

def overlap(i1, i2):
    # Assumes i1 <= i2
    if i1[0] <= i2[0] <= i1[1]:
        print(f'{i1} overlaps {i2}')
        return True
    print(f'{i1} does not overlap {i2}')
    return False

def merge_intervals(i1, i2):
    # Assumes i1 <= i2
    return [i1[0], max(i1[1], i2[1])]

def merge(intervals: List[List[int]]) -> List[List[int]]:
    if len(intervals) <= 1:
        return intervals
    
    intervals.sort();
    i = 0
    
    while i <= len(intervals)-2:
        print(f'i is {i}')
        print("Current: ", intervals)
        if overlap(intervals[i], intervals[i+1]):
            intervals[i] = merge_intervals(intervals[i], intervals[i+1])
            intervals.pop(i+1)
        else:
            i += 1
    
    return intervals

def main():
    i = [[1,3],[2,6],[8,10],[15,18]]
    print("Final: ", merge(i))

if __name__ == '__main__':
    main()
        