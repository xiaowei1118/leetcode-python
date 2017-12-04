# -*- coding: utf-8 -*-
'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

###最大子字符串
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    list = []
    max_size = 0
    i = 0
    while i < len(s):
        if not s[i] in list:
            list.append(s[i])
        else:
            max_size = max(max_size, len(list))
            list = list[list.index(s[i]) + 1:]
            list.append(s[i])

        i += 1

    max_size = max(max_size, len(list))

    return max_size


print lengthOfLongestSubstring("bbtablud")
