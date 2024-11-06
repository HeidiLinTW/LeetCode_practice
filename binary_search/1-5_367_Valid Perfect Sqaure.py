"""
https://leetcode.com/problems/valid-perfect-square/description/
Given a positive integer num, return true if num is a perfect square or false otherwise.
A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.
You must not use any built-in library function, such as sqrt.


Example 1:
Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.

Example 2:
Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.

Constraints:
1 <= num <= 2^31 - 1
"""


def isPerfectSquare( num: int) -> bool:
    if num == 1 or num == 0:
        return True
    left = 1
    right = num - 1
    while left <= right:
        middle = (left + right) // 2
        if middle ** 2 < num:
            left = middle + 1
        elif middle ** 2 > num:
            right = middle - 1
        else:
            return True
    return False


if __name__ == "__main__":
    # Example 1:
    # Input = 16
    # Output = True

    # Example 2:
    Input = 14
    Output = False

    answer = isPerfectSquare(Input)
    print(f"answer:{answer}, should be:{Output}")
