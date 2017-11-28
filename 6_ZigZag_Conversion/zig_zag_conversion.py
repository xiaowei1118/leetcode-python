# -*- coding=utf-8 -*-
'''
    The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

    P   A   H   N
    A P L S I I G
    Y   I   R
    And then read line by line: "PAHNAPLSIIGYIR"
    Write the code that will take a string and make this conversion given a number of rows:

    string convert(string text, int nRows);
    convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''


def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """

    result = ""
    for k in range(0, numRows):
        if numRows == 1:     # 如果是单行，直接返回字符串，不参与计算
            return s

        j = 2
        if k < len(s):
            bs = s[k]
        else:
            return result

        while True:
            next_line_right = j * (numRows - 1)
            index = next_line_right - k

            if k != numRows - 1 and k != 0:     # 收尾行没有斜线部分
                if index < len(s):
                    bs += s[index]
                else:
                    break

            if next_line_right + k < len(s):   # 输出Z字形的中间斜线部分
                bs += s[next_line_right + k]
            else:
                break
            j = j + 2

        result += bs

    return result


print convert("PAYPALISHIRING", 3)
