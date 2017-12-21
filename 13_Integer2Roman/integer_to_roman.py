# coding: utf-8
'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

 I（1）、V（5）、X（10）、L（50）、C（100）、D（500）和M（1000）
'''


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for index, item in enumerate(s):
            if index < len(s) - 1 and roman_dict[item] < roman_dict[s[index + 1]]:
                result -= roman_dict[item]
            else:
                result += roman_dict[item]

        return result


print(Solution().romanToInt("MMMCMXCIX"))
