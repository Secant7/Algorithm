#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#
# https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/description/
#
# algorithms
# Easy (52.03%)
# Likes:    372
# Dislikes: 0
# Total Accepted:    131.6K
# Total Submissions: 251.6K
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# 给定两个数组，编写一个函数来计算它们的交集。
# 
# 
# 
# 示例 1：
# 
# 输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2,2]
# 
# 
# 示例 2:
# 
# 输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[4,9]
# 
# 
# 
# 说明：
# 
# 
# 输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
# 我们可以不考虑输出结果的顺序。
# 
# 
# 进阶：
# 
# 
# 如果给定的数组已经排好序呢？你将如何优化你的算法？
# 如果 nums1 的大小比 nums2 小很多，哪种方法更优？
# 如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
# 
# 
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter 
        a = Counter(nums1)
        res = []
        for num in nums2:
            if num in a and a[num] > 0:
                a[num] -= 1 
                res.append(num)

        return res


        
# @lc code=end

