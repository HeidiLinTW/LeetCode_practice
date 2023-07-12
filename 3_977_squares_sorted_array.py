"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
"""


def sorted_squares(data: list[int]):
    for i in range(len(data)):
        data[i] *= data[i]

    data.sort()
    return data


def sorted_squares_2(data: list[int]):
    return sorted(x*x for x in data)


def sorted_squares_2_pointers(data: list[int]):
    i = 0
    j = len(data) - 1

    output = data.copy()
    k = len(data) - 1

    while j >= i:
        if data[j] ** 2 > data[i] ** 2:
            output[k] = data[j] ** 2
            j -= 1
        else:
            output[k] = data[i] ** 2
            i += 1

        k -= 1

    return output


if __name__ == "__main__":
    nums = [-4, -1, 0, 3, 10]
    # a = sorted_squares(nums)
    # print(a)
    # b = sorted_squares_2(nums)
    # print(b)
    print(sorted_squares_2_pointers(nums))
