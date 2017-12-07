# coding: utf-8

'''
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.
'''

import sys
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        return self.tackleFlag(str.strip(), "+")

    def tackleFlag(self, str, flag):
        if str and str[0] == "-":
            if flag == "-":
                return self.tackleFlag(str[1:], "+")
            else:
                return self.tackleFlag(str[1:], "-")

        if str and str[0] == "+":
            return self.tackleFlag(str[1:], flag)

        str_len = len(str)
        sum = 0
        for index, item in enumerate(str):
            if '0' <= item <= '9':
                #没有考虑整数溢出情况
                sum += (ord(item) - ord('0')) * 10 ** (str_len - index - 1)
            else:
                raise Exception(str + "包含非数字字符，转换异常")

        if str and flag == "-":
            return -sum

        return sum

print Solution().myAtoi("  -001242")
