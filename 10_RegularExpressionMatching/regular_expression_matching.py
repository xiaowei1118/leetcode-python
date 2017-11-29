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


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        if not p.__contains__(".") and not p.__contains__("*"):
            return s == p

        i = 0
        j = 0
        while j < len(p):
            if p[j] == ".":
                if i == len(s):
                    return False

                i += 1
                j += 1
            elif p[j] == "*":
                if p[j - 1] == ".":
                    k = len(s) - 1
                    if j == len(p) - 1:
                        return True

                    while k > i - 2:
                        flag = self.isMatch(s[k:], p[j + 1:])
                        if flag:
                            return flag
                        k -= 1

                    return False
                else:
                    ### ab  ac*b
                    if s[i - 1] != p[j - 1]:
                        return self.isMatch(s[i - 1:], p[j + 1:])
                    # abbc  ab*c
                    else:
                        m = p[j - 1]
                        i = i - 1
                        j = j + 1
                        while j < len(p):
                            if j < len(p) - 1 and p[j] == m and p[j + 1] == "*":
                                j = j + 2
                            elif p[j] == m and s[i] == m and i < len(s):
                                j += 1
                                i += 1
                            else:
                                break

                        for k in range(i, len(s)):
                            if s[k] != m:
                                return self.isMatch(s[k:], p[j:])
                        else:
                            if len(p) - j > len(s) - i:
                                return False
                            else:
                                for j in range(j + 1, len(p)):
                                    if s[i] != p[j]:
                                        return False
                                else:
                                    return True

            elif i < len(s) and s[i] != p[j]:
                if j < len(s) - 1:
                    if j == len(p) - 1 or p[j + 1] != '*':
                        return False

                i += 1
                j += 1
            else:
                if i == len(s):
                    return (p[j] == "*" and j == len(p) - 1) or (j == len(p) - 2 and p[j + 1] == "*")
                else:
                    i += 1
                    j += 1

        if i == len(s):
            for j in range(j, len(p)):
                if p[j] != "." and p[j] != "*":
                    return False

        if j == len(p):
            return p[j - 1] == "*" or (s[i - 1] == p[j - 1] and j == len(s))

        return True


print Solution().isMatch("aaa", "ab*a*c*a")
