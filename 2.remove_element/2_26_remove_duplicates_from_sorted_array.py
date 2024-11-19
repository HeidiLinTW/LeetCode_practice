"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially.
The remaining elements of nums are not important as well as the size of nums.
Return k.
"""


def rm_duplicates(input_array: list):
    slow = 0
    for fast in range(1, len(input_array)):
        if input_array[fast] != input_array[fast - 1]:
            slow += 1
            input_array[slow] = input_array[fast]

    return slow + 1, input_array


if __name__ == '__main__':
    # Example 1
    # Input:
    nums = [1, 1, 2]
    Output = 2  # nums = [1, 2, _]
    # # Example 2
    # # Input:
    # nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    # Output = 5  # nums = [0, 1, 2, 3, 4, _, _, _, _, _]

    print(rm_duplicates(nums))
