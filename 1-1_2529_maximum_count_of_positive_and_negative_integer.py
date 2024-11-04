"""
Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.

In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.
Note that 0 is neither positive nor negative.

https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/

[Example 1]:
Input: nums = [-2,-1,-1,1,2,3]
Output: 3
Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.

[Example 2]:
Input: nums = [-3,-2,-1,0,0,1,2]
Output: 3
Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.

[Example 3]:
Input: nums = [5,20,66,1314]
Output: 4
Explanation: There are 4 positive integers and 0 negative integers. The maximum count among them is 4.

[Constraints]:
1 <= nums.length <= 2000
-2000 <= nums[i] <= 2000
nums is sorted in a non-decreasing order.

"""


def maximumCount(nums: list[int]) -> int:
    pos_num = 0
    neg_num = 0
    for i in nums:
        if i > 0:
            pos_num += 1
        elif i < 0:
            neg_num += 1

    return max(pos_num, neg_num)


def maximumCount_2nd(nums: list[int]) -> int:  # Runtime 83.20%, Memory 50.70%
    if 0 in nums:
        nums[:] = (value for value in nums if value != 0)
        print(type(nums))
    if len(nums) > 0:
        if nums[0] > 0 or nums[-1] < 0:
            return len(nums)
        else:
            left, right = 0, len(nums) - 1
            print(f"{left=}")
            print(f"{right=}")

            pos = 0
            # neg = 0
            print(f"{pos=}")
            print(f"neg=0")
            print("-----------")
            while left <= right:
                middle = (left + right) // 2
                print(f"{middle=}")
                print(f"{nums[middle]=}")
                if nums[middle] < 0:
                    # neg += middle - left + 1
                    left = middle + 1
                    print(f"{left=}")
                    print(f"{right=}")
                    print(f"{pos=}")
                    print(f"neg={len(nums)-pos}")
                    print("-----------")
                elif nums[middle] > 0:
                    pos += right - middle + 1
                    right = middle - 1
                    print(f"{left=}")
                    print(f"{right=}")
                    print(f"{pos=}")
                    print(f"neg={len(nums)-pos}")
                    print("-----------")

            return max(pos, len(nums)-pos)
    else:
        return 0


def maximumCount_3rd(nums: list[int]) -> int:  # this method is from others, Runtime 96.30%, Memory 91.70%
    if nums[0] == nums[-1] == 0:  # 全0的case
        return 0
    else:
        if nums[0] > 0 or nums[-1] < 0:  # 全positive or 全negative的case
            return len(nums)
        else:
            # 找到positive & negative 的邊界 = right, left交錯的地方
            # left要往positive去
            # right要往negative去
            left, right = 0, len(nums) - 1
            print(f"{left=}")
            print(f"{right=}")

            while left <= right:
                print(f"{nums=}")
                middle = (left + right) // 2
                print(f"{middle=}")
                print(f"{nums[middle]=}")
                if nums[middle] < 0:
                    left = middle + 1
                    print(f"{left=}")
                    print(f"{right=}")
                elif nums[middle] > 0:
                    right = middle - 1
                    print(f"{left=}")
                    print(f"{right=}")
                else:  # 把0去掉
                    print("delete 0")
                    print(f"{left=}")
                    print(f"{right=}")
                    del nums[middle]
                print("-----------")

            return max(left, len(nums) - left)  # left = amount of negative


if __name__ == "__main__":

    # test_data_list = [([-2,-1,-1,1,2,3], 3), ([-3,-2,-1,0,0,1,2], 3), ([5,20,66,1314], 4)]
    # test_data_list = [([-1563,-236,-114,-55,427,447,687,752,1021,1636], 6)]
    test_data_list = [([-3, -2, -1, 0, 0, 1, 2], 3)]
    i = 1
    for test_data in test_data_list:
        answer = maximumCount_3rd(test_data[0])
        if answer == test_data[1]:
            print(f"test #{i} pass")
        else:
            print(f"test #{i} fail")
            print(f"return={answer}; answer={test_data[1]}")
        i += 1
