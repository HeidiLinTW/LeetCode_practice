"""
https://leetcode.com/problems/sqrtx/description/
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.


Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

Constraints:
0 <= x <= 2^31 - 1

"""


def find_sqrt(x: int) -> int:
    if x == 1 or x == 0:
        return x
    left = 1
    right = x - 1
    while left <= right:
        middle = (left + right) // 2
        if middle ** 2 < x:
            left = middle + 1
        elif middle ** 2 > x:
            right = middle - 1
        else:
            return middle
    return right  # right, left 交錯後，right**2 就會是最接近x但又<x的值


if __name__ == "__main__":
    # Example 1:
    # Input = 4
    # Output = 2
    # Example 2:
    Input = 8
    Output = 2

    answer = find_sqrt(Input)
    print(f"answer:{answer}, should be:{Output}")
