# coding: utf-8

# 全排列问题
def CalcAllPermutation(str):
    allArranged(str, 0, len(str) - 1)

def allArranged(str, first, last):
    if last <= 1:
        return

    if first == last:
        for i in range(last + 1):
            print str[i],

        print ""
    else:
        for i in range(first, last + 1):
            str = swap(str, i, first)
            allArranged(str, first + 1, last)
            str = swap(str, i, first)


def swap(str, i, j):
    str = list(str)
    temp = str[i]
    str[i] = str[j]
    str[j] = temp
    str = "".join(str)
    return str

CalcAllPermutation("abcd")