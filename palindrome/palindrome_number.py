"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

Example 1:
Input: x = 121
Output: true

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Example 4:
Input: x = -101
Output: false


Constraints:

-231 <= x <= 231 - 1

Follow up: Could you solve it without converting the integer to a string?
"""


def main(num):
    is_neg = False
    input_num = num

    if num < 0:
        is_neg = True
        num *= -1

    reverse = 0

    while num > 0:
        reminder = num % 10
        reverse = reverse * 10 + reminder
        num //= 10
    if is_neg:
        num *= -1

    return input_num == reverse


print(main(121))
print(main(123))
print(main(-123))
print(main(-121))


def sol2(num):
    if num < 0:
        return False
    return str(num) == str(num)[::-1]


print(sol2(121))
print(sol2(123))
print(sol2(-123))
print(sol2(-121))
