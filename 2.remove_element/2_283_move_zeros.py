"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

解法：
雙指標
fast指到的值非0時，nums[fast]和nums[slow]互換，slow++
"""


def moveZeros_heidi(nums: list[int]):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            if fast != slow:
                nums[fast] = 0
            slow += 1
    return nums


def moveZeros(nums: list[int]):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[fast], nums[slow] = nums[slow], nums[fast]
            slow += 1
    return nums


if __name__ == "__main__":
    # # Example 1:
    # # Input:
    # nums = [0, 1, 0, 3, 12]
    # # Output:
    # ans = [1, 3, 12, 0, 0]

    # Example 2:
    # Input:
    nums = [0]
    # Output:
    ans = [0]

    result = moveZeros(nums)
    print(f"result:{result}, answer:{ans}")
