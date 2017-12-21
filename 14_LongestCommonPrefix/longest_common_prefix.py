# coding: utf-8
'''
Write a function to find the longest common prefix string amongst an array of strings.
'''


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        prefix = strs[0]
        for index in xrange(1, len(strs)):
            prefix = self.findLongestCommonPrefixInTwoStr(strs[index], prefix)

        return prefix

    def findLongestCommonPrefixInTwoStr(self, str1, str2):
        if len(str1) > len(str2):
            str1, str2 = str2, str1

        for index, item in enumerate(str1):
            if item != str2[index]:
                return str1[:index]

        return str1


print(Solution().longestCommonPrefix(["leet", "leetcode", "leedodes", "leemod"]))
