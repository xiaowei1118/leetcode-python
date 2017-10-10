# -*- coding:utf-8 -*-
'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"
'''


def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    max_length = 0
    dict = {}
    for index, item in enumerate(s):
        if item in s[index+1:]:
            m = s.rindex(item)

            while m > 0:
                j = m
                for i in range(index, len(s)):
                    if i >= j:
                        # 回文
                        str = s[index:m+1]
                        max_length = max(len(s[index:m+1]),max_length)
                        dict[len(s[index:m+1])] = str
                        break

                    if s[i] != s[j]:
                        break
                    else:
                        i += 1
                        j -= 1

                m = s[:m].rindex(item)

    if len(dict) > 0:
        return dict[max_length]
    else:
        return s[0]

print longestPalindrome("aaabaaaa")