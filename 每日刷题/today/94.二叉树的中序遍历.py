#
# @lc app=leetcode.cn id=94 lang=python3
# @lcpr version=21907
#
# [94] 二叉树的中序遍历
#
# https://leetcode.cn/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Easy (76.20%)
# Likes:    1808
# Dislikes: 0
# Total Accepted:    1.1M
# Total Submissions: 1.5M
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。
# 
# 
# 
# 示例 1：
# 
# 输入：root = [1,null,2,3]
# 输出：[1,3,2]
# 
# 
# 示例 2：
# 
# 输入：root = []
# 输出：[]
# 
# 
# 示例 3：
# 
# 输入：root = [1]
# 输出：[1]
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数目在范围 [0, 100] 内
# -100 <= Node.val <= 100
# 
# 
# 
# 
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # 递归

        stack = []
        res = []

        node = root 

        while node or stack:
            if node:
                stack.append(node)
                node = node.left 
            else:
                temp = stack.pop()
                res.append(temp.val)
                node = temp.right
        return res 

                

        
# @lc code=end



#
# @lcpr case=start
# [1,null,2,3]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

        # #递归
        # res = []

        # def helper(root):
        #     if not root:
        #         return 
        #     helper(root.left)
        #     res.append(root.val)
        #     helper(root.right) 

        # helper(root)

        # return res 