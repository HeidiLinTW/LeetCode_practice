"""
https://leetcode.com/problems/remove-element/description/
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

1.
Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
The remaining elements of nums are not important as well as the size of nums.

2.
Return k.
"""


def removeElement(nums: list[int], val: int) -> int:
    if len(nums) == 0:
        return 0
    else:
        nums_copy = nums.copy()
        for number in nums_copy:
            if number == val:
                nums.remove(val)
        print(nums)
        return len(nums)


def removeElement_2_pointers(nums: list[int], val: int) -> int:
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
    return slow


if __name__ == "__main__":
    input_data = [0,1,2,2,3,0,4,2]
    result = removeElement_2_pointers(input_data, 2)
    print(result)




