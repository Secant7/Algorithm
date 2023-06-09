#
# @lc app=leetcode.cn id=713 lang=python3
#
# [713] 乘积小于K的子数组
#
# https://leetcode-cn.com/problems/subarray-product-less-than-k/description/
#
# algorithms
# Medium (43.99%)
# Likes:    478
# Dislikes: 0
# Total Accepted:    60.9K
# Total Submissions: 128.8K
# Testcase Example:  '[10,5,2,6]\n100'
#
# 给你一个整数数组 nums 和一个整数 k ，请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目。
#
#
# 示例 1：
#
#
# 输入：nums = [10,5,2,6], k = 100
# 输出：8
# 解释：8 个乘积小于 100 的子数组分别为：[10]、[5]、[2],、[6]、[10,5]、[5,2]、[2,6]、[5,2,6]。
# 需要注意的是 [10,5,2] 并不是乘积小于 100 的子数组。
#
#
# 示例 2：
#
#
# 输入：nums = [1,2,3], k = 0
# 输出：0
#
#
#
# 提示:
#
#
# 1 <= nums.length <= 3 * 10^4
# 1 <= nums[i] <= 1000
# 0 <= k <= 10^6
#
#
#


# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        n = len(nums)
        logprefix = [0] * (n + 1)
        for i in range(n):
            logprefix[i + 1] = logprefix[i] + log(nums[i])
        logk = log(k)
        ans = 0
        for j in range(1, n + 1):
            l = bisect_right(logprefix, logprefix[j] - logk + 1e-10, 0, j)
            ans += j - l
        return ans


# @lc code=end
# def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
#     i, prod, ans = 0, 1, 0  #
#     for j, num in enumerate(nums):
#         prod *= num
#         while i <= j and prod >= k:
#             prod //= nums[i]
#             i += 1
#         ans += j - i + 1
#     return ans
