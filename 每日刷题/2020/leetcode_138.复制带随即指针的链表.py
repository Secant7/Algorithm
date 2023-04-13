#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 复制带随机指针的链表
#
# https://leetcode-cn.com/problems/copy-list-with-random-pointer/description/
#
# algorithms
# Medium (58.79%)
# Likes:    449
# Dislikes: 0
# Total Accepted:    54.2K
# Total Submissions: 92K
# Testcase Example:  '[[7,null],[13,0],[11,4],[10,2],[1,0]]'
#
# 给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。
# 
# 要求返回这个链表的 深拷贝。 
# 
# 我们用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：
# 
# 
# val：一个表示 Node.val 的整数。
# random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# 输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
# 
# 
# 示例 2：
# 
# 
# 
# 输入：head = [[1,1],[2,1]]
# 输出：[[1,1],[2,1]]
# 
# 
# 示例 3：
# 
# 
# 
# 输入：head = [[3,null],[3,0],[3,null]]
# 输出：[[3,null],[3,0],[3,null]]
# 
# 
# 示例 4：
# 
# 输入：head = []
# 输出：[]
# 解释：给定的链表为空（空指针），因此返回 null。
# 
# 
# 
# 
# 提示：
# 
# 
# -10000 <= Node.val <= 10000
# Node.random 为空（null）或指向链表中的节点。
# 节点数目不超过 1000 。
# 
# 
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# class Solution:
#     def __init__(self):
#         self.visited = {}
        
#     def copyRandomList(self, head: 'Node') -> 'Node':
        
#         if not head:
#             return 
        
#         if head in self.visited:
#             return self.visited[head]
        
#         node = Node(head.val,None,None)
        
#         self.visited[head] = node  
        
#         node.next = self.copyRandomList(head.next)
#         node.random = self.copyRandomList(head.random)
        
#         return node
class Solution:
   
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return  
        
        p = head  
        
        while p:
            new_node = Node(p.val,None,None)
            new_node.next = p.next  
            p.next = new_node 
            p = new_node.next  
            
        p = head  
        
        while p:
            if p.random:
                p.next.random = p.random.next  
            p = p.next.next  
            
        p = head  
        
        dummy = Node(-1,None,None)
        
        cur = dummy  
        
        while p:
            cur.next = p.next 
            cur = cur.next   
            
            p.next = cur.next  
            p = p.next  
            
        return dummy.next 
        
        


        
