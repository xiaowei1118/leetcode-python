# coding: utf-8

# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
#
# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

# 1 -> ''  2 -> 'abc' 3 -> def 4 -> ghi 5->jkl 6->mno  7->pqrs 8->tuv 9->wxyz
# 示例:
#
# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
# 说明:
# 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

class Solution(object):

    # 使用递归
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        list = []

        dict = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
        }

        if not len(digits):   # 考虑空字符串
            return []

        if len(digits) == 1:
            for x in dict[int(digits)]:
                list.append(x)

            return list

        sublist = self.letterCombinations(digits[0:len(digits) - 1])
        for item in sublist:
            for letter in dict[int(digits[len(digits) - 1])]:
                list.append(item + letter)

        return list


digits = '23'
print Solution().letterCombinations(digits)
