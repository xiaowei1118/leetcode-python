# coding: utf-8

'''
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
'''


def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """

    if not p.__contains__(".") and not p.__contains__("*"):
        return s == p

    i = 0
    j = 0
    while i < len(s) and j < len(p):
        if s[i] != p[j]:
            if p[j] == ".":
                pass
            elif p[j] == "*":
                if p[j - 1] == ".":
                    pass
                    # i = len(s)
                    # break
                elif i > 0 and s[i] == p[j - 1]:
                        return isMatch(s[i + 1:], p[j + 1:]) or isMatch(s[i:], p[j + 1:])
                else:
                    return isMatch(s[i - 1:], p[j + 1:])

        i += 1
        j += 1

    if i == len(s):
        for j in range(j, len(p)):
            if p[j] != "." and p[j] != "*":
                return False

    if j == len(p):
        return p[j - 1] == "*"

    return True


print isMatch("aab", ".*")
