def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """

    result = ""
    for k in range(0, numRows):
        j = 2
        if k < len(s):
            bs = s[k]
        else:
            return result

        while True:
            index = j * (numRows - 1) - k

            if k != numRows - 1:
                if index < len(s):
                    bs += s[index]
                else:
                    break
            else:
                if j * (numRows - 1) + k < len(s):
                    bs += s[j * (numRows - 1) + k]
                else:
                    break
            j = j + 2

        result += bs

    return result

print convert("A", 2)
