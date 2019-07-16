# coding: utf-8
'''
  Determine whether an integer is a palindrome. Do this without extra space.
'''

### 判断一个整数是不是一个回文整数，注意，负数不是回文整数
import math

def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False

    n = 0
    ## n代表x的位数
    for i in range(0, 100):
        if x / math.pow(10, i) > 0 and x / math.pow(10, i) < 10:
            n = i
            break

    i = 1
    j = n + 1
    while i <= j:
        if math.floor(x % math.pow(10, i) / math.pow(10, i - 1)) != math.floor(
                                x % math.pow(10, j) / math.pow(10, j - 1)):
            return False

        i += 1
        j -= 1

    return True


print isPalindrome(1)
