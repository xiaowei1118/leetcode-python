# -*- coding=utf-8 -*-
'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output:  321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note:
    Assume we are dealing with an environment which could only hold integers within the
    32-bit signed integer range. For the purpose of this problem, assume that your
    function returns 0 when the reversed integer overflows.
'''
import math


def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x >= math.pow(2, 31) or x <= - math.pow(2, 31):  # 32位的数字，第一位是符号位，所以是2的31次方
        return 0

    reverse_str = str(x)[::-1]
    if reverse_str[0] == "0" and x != 0:
        reverse_str = reverse_str[1:]

    if x < 0:
        reverse_str = "-" + reverse_str[0:len(reverse_str) - 1]

    result = int(reverse_str)
    return result if result < math.pow(2, 31) and result > - math.pow(2, 31) else 0

print reverse(1563847412)