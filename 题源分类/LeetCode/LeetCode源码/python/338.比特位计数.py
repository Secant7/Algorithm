#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#
# https://leetcode-cn.com/problems/counting-bits/description/
#
# algorithms
# Medium (76.66%)
# Likes:    604
# Dislikes: 0
# Total Accepted:    101.4K
# Total Submissions: 128.8K
# Testcase Example:  '2'
#
# 给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
# 
# 示例 1:
# 
# 输入: 2
# 输出: [0,1,1]
# 
# 示例 2:
# 
# 输入: 5
# 输出: [0,1,1,2,1,2]
# 
# 进阶:
# 
# 
# 给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
# 要求算法的空间复杂度为O(n)。
# 你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。
# 
# 
#

# @lc code=start
class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0]*(num+1)
        for i in range(1,num+1):
            dp[i] = dp[i-1]+1 if i % 2 == 1 else dp[i//2]
        
        return dp

# @lc code=end

# def countBits(self, num: int) -> List[int]:
#     ans = []
#     def count(num):
#         if num == 0:
#             return 0 
#         if num % 2 == 1:
#             return count(num-1)+1
#         return count(num//2)
#     for i in range(num+1):
#         ans.append(count(i))
    
#     return ans 



# def countBits(self, num: int) -> List[int]:
#     memo = [0]*(num+1)
#     def count(num):
            
#         if num == 0:
#             return 0 
#         if memo[num]:
#             return memo[num]
#         if num % 2 == 1:
#             res = count(num-1)+1
#         else:
#             res = count(num//2)
#         memo[num] = res
#         return res

#     res = []
#     for i in range(num+1):
#         res.append(count(i))
#     return res 