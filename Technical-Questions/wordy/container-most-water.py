# INPUT: Array of non-negative integers
# OUTPUT: Greatest possible area of any rectangle formed between two "lines"
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum_area = 0
        left = 0
        right = len(height)-1

        while left < right:
            current_area = (right - left) * min(height[left], height[right])
            if current_area > maximum_area:
                maximum_area = current_area
            print("Left", height[left], "right", height[right])
            if height[left] >= height[right]:
                print("move left")
                right -= 1
            else:
                print("move right")
                left += 1

        return maximum_area


def main():
    solution = Solution()
    numbers = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(solution.maxArea(numbers))


if __name__ == '__main__':
    main()
