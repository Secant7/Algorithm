#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (64.39%)
# Likes:    780
# Dislikes: 0
# Total Accepted:    222K
# Total Submissions: 344.2K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
# 
# 示例 1:
# 
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
# 
# 
# 示例 2:
# 
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
# 
# 说明: 
# 
# 你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
# 
#

# @lc code=start
import heapq as pq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        
        return pq.nlargest(k, nums)[-1]
            
            
# @lc code=end
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     nums.sort(reverse=True)
    #     return nums[k-1]
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     queue = []
    #     for i in range(len(nums)):
    #         pq.heappush(queue,nums[i])
    #         if len(queue) > k:
    #             pq.heappop(queue)
        
    #     return queue[0]