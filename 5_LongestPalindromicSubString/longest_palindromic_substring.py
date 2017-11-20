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
        if item in s[index + 1:]:
            m = s.rindex(item)

            while m > 0:
                j = m
                for i in range(index, len(s)):
                    if i >= j:
                        # 回文
                        str = s[index:m + 1]
                        max_length = max(len(s[index:m + 1]), max_length)
                        dict[len(s[index:m + 1])] = str
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


# 动态规划
# P(i, j) = ( P(i+1, j-1)  and S_i == S_j ) P(i,j)=(P(i+1,j−1) and S(​i)==S​(j)
# p(i,i) = true and  p(i,i+1) == (S_i == S_i+1)

def getPalindrome(s, start, end):
    i = 0
    while i < start + 1 and i < len(s) - end:
        if s[start - i] != s[end + i]:
            i -= 1
            break

        i += 1
    else:
        i -= 1

    return s[start - i:end + i + 1]

def longestPalindrome_dynamic(s):
    max_palindrome = s[0]
    for index, value in enumerate(s):
        palindrome_middle = getPalindrome(s, index, index)
        if len(max_palindrome) < len(palindrome_middle):
            max_palindrome = palindrome_middle

        if index < len(s)-1 and value == s[index + 1]:
            palindrome = getPalindrome(s, index, index + 1)
            if len(palindrome) > len(max_palindrome):
                max_palindrome = palindrome

    return max_palindrome


# print longestPalindrome("aaabaaaa")
print longestPalindrome_dynamic("aaabaaa")
