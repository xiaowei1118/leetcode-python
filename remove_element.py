# -*- coding=utf-8 -*-
# 从数组中移除指定值
def remove_element(list, a):
    k = 0
    for i in range(len(list)):
        if list[i] == a:
            for j in range(i + 1, len(list)):
                if list[j] != a:
                    temp = list[i]
                    list[i] = list[j]
                    list[j] = temp
                    k += 1
                    break
        else:
            k += 1

    return k,list[:k]

list = [1,2,5,5,10,7,8,10]
print remove_element(list,5)
