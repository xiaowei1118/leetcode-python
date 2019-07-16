# -*- coding=utf-8 -*-
# 从数组中移除指定值
def remove_element(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] == val:
            for j in range(i + 1, len(nums)):
                if nums[j] != val:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
                    k += 1
                    break
        else:
            k += 1

    return nums[:k]

list = [3,2,2,3]
print remove_element(list,2)
