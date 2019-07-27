# coding=utf-8
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
# #
# # 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
# #
# # 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
# #
# # 来源：力扣（LeetCode）
# # 链接：https://leetcode-cn.com/problems/3sum-closest

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        list = []
        diff = None

        i = 0
        while i < len(nums) - 1:
            if target > 0 and nums[i] >= target and i < len(nums) - 2:  # 如果nums[i] > target 则三数之和必然大于target，且后续只会更大
                item = [nums[i], nums[i + 1], nums[i + 2]]
                if not diff or abs(sum(item) - target) < diff:
                    list = item

                break

            j = i + 1
            p = len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:  # 对 i 去重, 不能用i和i+1比较，因为i+1和i可能是一堆，可以用i和i-1比较，应该i已经被当成j用过
                i = i + 1
                continue

            while j < p:
                item = [nums[i], nums[j], nums[p]]
                if not diff or abs(sum(item) - target) < diff:
                    diff = abs(sum(item) - target)
                    list = item

                latestDiff = sum(item) - target
                if latestDiff > 0:
                    p = p - 1
                elif latestDiff < 0:
                    j = j + 1
                else:
                    return sum(item)

            i = i + 1

        return sum(list)


# nums = [6,-18,-20,-7,-15,9,18,10,1,-20,-17,-19,-3,-5,-19,10,6,-11,1,-17,-15,6,17,-18,-3,16,19,-20,-3,-17,-15,-3,12,1,-9,4,1,12,-2,14,4,-4,19,-20,6,0,-19,18,14,1,-15,-5,14,12,-4,0,-10,6,6,-6,20,-8,-6,5,0,3,10,7,-2,17,20,12,19,-13,-1,10,-1,14,0,7,-3,10,14,14,11,0,-4,-15,-8,3,2,-5,9,10,16,-4,-3,-9,-8,-14,10,6,2,-12,-7,-16,-6,10]
nums = [-20, -20, -20, -20, -19, -19, -19, -18, -18, -17, -17, -17, -16, -15, -15, -15, -15, -15, -14, -13, -12, -11,
        -10, -9, -9, -8, -8, -8, -7, -7, -6, -6, -6, -5, -5, -5, -4, -4, -4, -4, -3, -3, -3, -3, -3, -3, -2, -2, -1, -1,
        0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 9, 9, 10, 10, 10, 10, 10, 10, 10,
        10, 11, 12, 12, 12, 12, 14, 14, 14, 14, 14, 14, 16, 16, 17, 17, 18, 18, 19, 19, 19, 20, 20]
print Solution().threeSumClosest(nums, -52)
