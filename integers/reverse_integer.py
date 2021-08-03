"""

Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Example 4:
Input: x = 0
Output: 0


Constraints:

-231 <= x <= 231 - 1
"""


def main(num):
    is_neg = False
    if num < 0:
        is_neg = True
        num = -1 * num
    result = 0
    while num > 0:
        reminder = num % 10
        result = result * 10 + reminder
        num = num // 10
    if is_neg:
        result = -1 * result
    if result > (2 ** 31 - 1) or result < -(2 ** 31 - 1):
        return 0
    return result


print(main(123))
print(main(120))
print(main(123451111111116))
print(main(-2233))
