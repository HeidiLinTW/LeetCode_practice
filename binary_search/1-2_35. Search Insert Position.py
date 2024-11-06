"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4


Constraints:

a. 1 <= nums.length <= 10000
b. -10000 < nums[i], target < 10000
c. nums contains distinct values sorted in ascending order.

"""


def solution_heidi(array: list[int], target:int) -> int:
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        if array[middle] == target:
            # print(f"middle:{middle}")
            return middle
        elif array[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    # print(f"left:{left}, right:{right}")
    return left
    # my thought:
    # the cases that the number is not found in the list
    #  1, 3, 5, 6
    # ^  ^  ^  ^  ^
    # |  |  |  |  |
    # a  b  c  d  e => cases

    # after I printed (left, right) out when these cases happened
    # case a: (left, right) = (0, -1)
    # case b: (left, right) = (1, 0)
    # case c: (left, right) = (2, 1)
    # case d: (left, right) = (3, 2)
    # case e: (left, right) = (4, 3)
    # so just return left when the number is not found in the list


if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    target = 5
    answer = solution_heidi(nums, target)
    print(f"answer: {answer}")
