# coding: utf-8

'''
    Given an integer, convert it to a roman numeral.

    Input is guaranteed to be within the range from 1 to 3999.

    I（1）、V（5）、X（10）、L（50）、C（100）、D（500）和M（1000）

    2.1 在较大的罗马数字的右边记上较小的罗马数字，表示大数字加小数字。
    2.2 在较大的罗马数字的左边记上较小的罗马数字，表示大数字减小数字。
    2.3 左减的数字有限制，仅限于I、X、C。比如45不可以写成VL，只能是XLV
    2.4 但是，左减时不可跨越一个位数。比如，99不可以用IC（100 - 1）表示，而是用XCIX（[100 - 10] + [10 - 1]）表示。（等同于阿拉伯数字每位数字分别表示。）
    2.5 左减数字必须为一位，比如8写成VIII，而非IIX。
    2.6 右加数字不可连续超过三位，比如14写成XIV，而非XIIII。（见下方“数码限制”一项。）

    4、数码限制：
    4.1 同一数码最多只能出现三次，如40不可表示为XXXX，而要表示为XL。
    4.2 例外：由于IV是古罗马神话主神朱庇特（即IVPITER，古罗马字母里没有J和U）的首字，因此有时用IIII代替IV

'''


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ""
        for i in range(0, 4):
            item = num % 10 ** (4 - i) / 10 ** (3 - i)

            if item > 5:
                if item < 9:
                    if i == 1:
                        result += "D" + "C" * (item - 5)
                    elif i == 2:
                        result += "L" + "X" * (item - 5)
                    elif i == 3:
                        result += "V" + "I" * (item - 5)
                else:
                    if i == 1:
                        result += "CM"
                    elif i == 2:
                        result += "XC"
                    elif i == 3:
                        result += "IX"
            elif item > 0:
                if item < 4:
                    if i == 0:
                        result += "M" * item
                    elif i == 1:
                        result += "C" * item
                    elif i == 2:
                        result += "X" * item
                    elif i == 3:
                        result += "I" * item
                elif item == 4:
                    if i == 1:
                        result += "CD"
                    elif i == 2:
                        result += "XL"
                    elif i == 3:
                        result += "IV"
                else:
                    if i == 1:
                        result += "D"
                    elif i == 2:
                        result += "L"
                    elif i == 3:
                        result += "V"

        return result


print(Solution().intToRoman(125))
