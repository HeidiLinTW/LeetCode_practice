"""
给定一个n个元素有序的（升序）整型数组nums 和一个目标值target，写一个函数搜索nums中的 target，如果目标值存在返回下标，否则返回 -1。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/binary-search
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def search_target_heidi(search_list: list[int], target: int) -> int:
    # O(n)
    index = -1
    list_len = len(search_list)
    for i in range(list_len):
        if search_list[i] == target:
            index = i
    return index


def search_binary(nums: list[int], target: int) -> int:
    # [left, right]
    # O(log n)
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] > target:
            right = middle - 1
        elif nums[middle] < target:
            left = middle + 1
        else:
            return middle
    return -1


def search_binary_right_open(nums: list[int], target: int) -> int:
    # [left, right)
    # O(log n)
    left = 0
    right = len(nums)
    while left < right:
        middle = (left + right) // 2
        if nums[middle] > target:
            right = middle
        elif nums[middle] < target:
            left = middle + 1
        else:
            return middle
    return -1


if __name__ == '__main__':
    # search_list = [-1,0,3,5,9,12]
    # target = 9
    nums_list = [-1,0,3,5,9,12]
    find = 2
    search_result = search_binary(nums_list, find)
    print(f"{search_result=}")
