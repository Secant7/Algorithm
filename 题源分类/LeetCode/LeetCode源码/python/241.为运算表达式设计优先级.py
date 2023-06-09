#
# @lc app=leetcode.cn id=241 lang=python3
#
# [241] 为运算表达式设计优先级
#
# https://leetcode-cn.com/problems/different-ways-to-add-parentheses/description/
#
# algorithms
# Medium (72.05%)
# Likes:    287
# Dislikes: 0
# Total Accepted:    17.2K
# Total Submissions: 23.8K
# Testcase Example:  '"2-1-1"'
#
# 给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及
# * 。
# 
# 示例 1:
# 
# 输入: "2-1-1"
# 输出: [0, 2]
# 解释: 
# ((2-1)-1) = 0 
# (2-(1-1)) = 2
# 
# 示例 2:
# 
# 输入: "2*3-4*5"
# 输出: [-34, -14, -10, -10, 10]
# 解释: 
# (2*(3-(4*5))) = -34 
# ((2*3)-(4*5)) = -14 
# ((2*(3-4))*5) = -10 
# (2*((3-4)*5)) = -10 
# (((2*3)-4)*5) = 10
# 
#

# @lc code=start
class Solution:
    memo = {}
    def diffWaysToCompute(self, input: str) -> List[int]:
        if input in Solution.memo:
            return Solution.memo[input]
        if input.isdigit():
            return [int(input)]
        res = []
        for i in range(len(input)):
            if input[i] in ["*","-","+"]:
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                
                for a in left:
                    for b in right:
                        if input[i] == "*":
                            res.append(a*b)
                            
                        if input[i] == "-":
                            res.append(a-b)
                            
                        if input[i] == "+":
                            res.append(a+b)
        Solution.memo[input] = res                              
        return res  
        

                
            
# @lc code=end

    # def diffWaysToCompute(self, input: str) -> List[int]:
        
    #     res = []
    #     n = len(input)
    #     for i in range(n):
    #         if input[i] in ["*","-","+"]:
    #             left = self.diffWaysToCompute(input[:i])
    #             right = self.diffWaysToCompute(input[i+1:])
                
    #             for a in left:
    #                 for b in right:
    #                     if input[i] == "+":
    #                         res.append(a+b)
    #                     if input[i] == "-":
    #                         res.append(a-b)
                            
    #                     if input[i] == "*":
    #                         res.append(a*b)
    #     if len(res) == 0:
    #         res.append(int(input))
    #     return res 
                