#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 省份数量
#
# https://leetcode-cn.com/problems/number-of-provinces/description/
#
# algorithms
# Medium (61.46%)
# Likes:    503
# Dislikes: 0
# Total Accepted:    118.5K
# Total Submissions: 192.9K
# Testcase Example:  '[[1,1,0],[1,1,0],[0,0,1]]'
#
# 
# 
# 有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c
# 间接相连。
# 
# 省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
# 
# 给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而
# isConnected[i][j] = 0 表示二者不直接相连。
# 
# 返回矩阵中 省份 的数量。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# 输出：2
# 
# 
# 示例 2：
# 
# 
# 输入：isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# 输出：3
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# n == isConnected.length
# n == isConnected[i].length
# isConnected[i][j] 为 1 或 0
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int: # 并查集
        provinces = len(isConnected)
        parent = [i for i in range(provinces)]
        
        def find(index):
            if parent[index] != index:
                parent[index] = find(parent[index])
            
            return parent[index]
        
        
        def union(index1,index2):
            parent[find(index1)] = find(index2)
            
        
        for i in range(provinces):
            for j in range(i+1,len(isConnected[i])):
                if isConnected[i][j] == 1:
                    union(i,j)
                    
        return sum(parent[i] == i for i in range(provinces))
            
            
                    
                
                    
                
        

            
        
        
        
# @lc code=end

    # def findCircleNum(self, isConnected: List[List[int]]) -> int: # DFS
    #     provinces = len(isConnected)
    #     visited = set()
    #     count = 0 
        
    #     def dfs(i):
    #         for j in range(provinces):
    #             if isConnected[i][j] == 1 and j not in visited:
    #                 visited.add(j)
    #                 dfs(j)
                    
    #     for i in range(provinces):
    #         if i not in visited:
    #             dfs(i)
    #             count += 1 
                
    #     return count 
            
            
    # def findCircleNum(self, isConnected: List[List[int]]) -> int: # BFS
    #     provinces = len(isConnected)
    #     visited = set() 
    #     count = 0 
    #     que = []
    #     for i in range(provinces):
    #         if i not in visited:
    #             que.append(i)
    #             while que:
    #                 province = que.pop(0)
    #                 visited.add(province)
    #                 for j in range(len(isConnected[province])):
    #                     if isConnected[province][j] == 1 and j not in visited:
    #                         que.append(j)
    #             count += 1
            
    #     return count
                    
                