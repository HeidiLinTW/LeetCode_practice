"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.



Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]


Constraints:

a. 0 <= nums.length <= 10^5
b. -10^9 <= nums[i] <= 10^9
c. nums is a non-decreasing array.
d. -10^9 <= target <= 10^9
"""

"""
解答影片
https://youtu.be/441pamgku74
"""


def solution(array: list[int], target_int: int) -> list[int]:

    def find_boundary(nums: list[int], target: int, is_left_most: bool) -> int:
        left = 0
        right = len(nums) - 1
        index = -1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:  # middle == target
                index = middle
                if is_left_most:  # 要找left most的index, 要繼續往左找, 所以right要繼續往左移, 直到right超過left, index就是left most
                    right = middle - 1
                else:  # 要找left most的index, 所以left要繼續往右移
                    left = middle + 1
        return index

    left_most = find_boundary(array, target_int, True)
    right_most = find_boundary(array, target_int, False)
    return [left_most, right_most]


if __name__ == "__main__":
    # Example 1:
    # Input:
    # nums = [5,7,7,8,8,10]
    # target = 8
    # Output = [3,4]
    #
    # Example 2:
    # Input:
    # nums = [5,7,7,8,8,10]
    # target = 6
    # Output = [-1,-1]
    #
    # Example 3:
    # Input:
    # nums = []
    # target = 0
    # Output = [-1,-1]

    answer = solution(nums, target)
    print(f"answer: {answer}, should be: {Output}")