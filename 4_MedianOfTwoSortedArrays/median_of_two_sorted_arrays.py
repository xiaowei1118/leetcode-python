# -*- coding:utf-8 -*-
'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''


def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    n = len(nums1)
    m = len(nums2)

    if n < m:
        n, m, nums1, nums2 = m, n, nums2, nums1

    if m == 0:
        if n % 2 == 1:
            return nums1[n / 2]
        else:
            return (nums1[n / 2] + nums1[(n - 1) / 2]) * 1.0 / 2

    min_i, max_i, half_len = 0, n , (n + m) / 2

    while min_i <= max_i:
        i = (min_i + max_i) / 2
        j = half_len - i
        if i < n and nums2[(j - 1) if j < m else m-1] > nums1[i]:
            min_i = i + 1
        elif i >= 0 and nums1[(i - 1) if i<n else n-1] > nums2[j if j < m else m-1]:
            max_i = i - 1
        else:
            if i == -1:
                max_of_left = nums2[(j - 1) if j<m else m-1]
            elif j == -1:
                max_of_left = nums1[(i - 1) if i<n else n-1]
            else:
                max_of_left = max(nums2[(j - 1) if j < m else m-1], nums1[(i - 1) if i<n else n-1])

            if (m + n) % 2 == 1:
                return max_of_left
            else:
                if i == n:
                    min_of_right = nums2[j-1]
                elif j == m:
                    min_of_right = nums1[i-1]
                else:
                    min_of_right = min(nums2[j-1], nums1[i-1])

                return (min_of_right + max_of_left) * 1.0 / 2


print findMedianSortedArrays([1, 2], [3,4,5,6])
