# coding: utf-8

# 给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
# 在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/container-with-most-water


class Solution(object):

    # 递归做法
    def maxArea1(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)

        if n == 2:
            return height[0] if height[0] < height[1] else height[1]

        maxArea = self.maxArea(height[0:n - 1])

        for j, item in enumerate(height):
            x = n - 1 - j  # x轴距离
            y = min(item, height[n-1]) # y轴距离

            area = x * y
            if (maxArea < area):
                maxArea = area

        return maxArea

    # 去除尾递归
    def maxArea2(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)

        maxArea = 0
        j = 1
        while j < n:
            i = 0
            while i < j:
                x = j - i  # x轴距离
                y = min(height[i], height[j])  # y轴距离

                area = x * y
                if (maxArea < area):
                    maxArea = area

                i = i + 1

            j = j + 1

        return maxArea

    # 双指针法
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)

        maxArea = 0
        i = 0
        j = n - 1

        while i < j:
            x = j - i  # x轴距离
            y = min(height[i], height[j])  # y轴距离

            area = x * y
            if (maxArea < area):
                maxArea = area

            if height[j] > height[i]:
                i = i + 1
            else:
                j = j - 1

        return maxArea

list = [1,8,6,2,5,4,8,3,7]
print Solution().maxArea(list)
