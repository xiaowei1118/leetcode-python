'''
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    Example:
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
'''

import copy
def two_sum(nums, target):
    for index, item in enumerate(nums):
            a = target - item
            list = copy.copy(nums)
            del list[index]
            if a in list:
                if nums.index(a) == index:
                    return [index,list.index(a)+1]
                return [index, nums.index(a)]

print(two_sum([-1,-2,-3,-4,-5], -8))
