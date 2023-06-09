#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#
# https://leetcode-cn.com/problems/binary-tree-preorder-traversal/description/
#
# algorithms
# Medium (65.89%)
# Likes:    291
# Dislikes: 0
# Total Accepted:    123.3K
# Total Submissions: 186.9K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的 前序 遍历。
# 
# 示例:
# 
# 输入: [1,null,2,3]  
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3 
# 
# 输出: [1,2,3]
# 
# 
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []  
        node = root  
        stack = []
        res = []
        while stack or node:
            while node:
                stack.append(node)
                res.append(node.val)
                node = node.left 
                
    
                 
            node = stack.pop()
            node = node.right 
        return res 
# @lc code=end

    # def preorderTraversal(self, root: TreeNode) -> List[int]:
    #     if not root:
    #         return []
    #     stack = [root]
    #     res = []
    #     while stack:
    #         node = stack.pop()
    #         res.append(node.val)
    #         if node.right:
    #             stack.append(node.right)
    #         if node.left:
    #             stack.append(node.left)
    #     return res
    
    
        # def preorderTraversal(self, root: TreeNode) -> List[int]:
        # if not root:
        #     return []  
        # node = root  
        # stack = []
        # res = []
        # while stack or node:
        #     if node:
        #         stack.append(node)
        #         res.append(node.val)
        #         node = node.left 
                 
                
        #     else:
        #         node = stack.pop()
        #         node = node.right
        # return res 