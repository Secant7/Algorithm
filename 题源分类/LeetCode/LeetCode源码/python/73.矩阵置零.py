#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#
# https://leetcode-cn.com/problems/set-matrix-zeroes/description/
#
# algorithms
# Medium (56.01%)
# Likes:    360
# Dislikes: 0
# Total Accepted:    66K
# Total Submissions: 117.8K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# 给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。
#
# 示例 1:
#
# 输入:
# [
# [1,1,1],
# [1,0,1],
# [1,1,1]
# ]
# 输出:
# [
# [1,0,1],
# [0,0,0],
# [1,0,1]
# ]
#
#
# 示例 2:
#
# 输入:
# [
# [0,1,2,0],
# [3,4,5,2],
# [1,3,1,5]
# ]
# 输出:
# [
# [0,0,0,0],
# [0,4,5,0],
# [0,3,1,0]
# ]
#
# 进阶:
#
#
# 一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
# 一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
# 你能想出一个常数空间的解决方案吗？
#
#
#


# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cols = len(matrix[0])
        rows = len(matrix)
        col0 = any(matrix[i][0] == 0 for i in range(rows))
        row0 = any(matrix[0][j] == 0 for j in range(cols))

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if row0:
            for i in range(cols):
                matrix[0][i] = 0

        if col0:
            for j in range(rows):
                matrix[j][0] = 0


# @lc code=end

# def setZeroes(self, matrix: List[List[int]]) -> None:
#     """
#     Do not return anything, modify matrix in-place instead.
#     """
#     cols = len(matrix[0])
#     rows = len(matrix)

#     if not cols or not rows:
#         return
#     row,col = False,False
#     for i in range(cols):
#         if matrix[0][i] == 0:
#             row = True
#             break

#     for j in range(rows):
#         if matrix[j][0] == 0:
#             col = True
#             break

#     for i in range(1,rows):
#         for j in range(1,cols):
#             if matrix[i][j] == 0:
#                 matrix[i][0] = 0
#                 matrix[0][j] = 0

#     for i in range(1,rows):
#         for j in range(1,cols):
#             if matrix[i][0] == 0 or matrix[0][j] == 0:
#                 matrix[i][j] = 0

#     if row:
#         for i in range(cols):
#             matrix[0][i] = 0

#     if col:
#         for i in range(rows):
#             matrix[i][0] = 0

#     return matrix

# def setZeroes(self, matrix: List[List[int]]) -> None:
# """
# Do not return anything, modify matrix in-place instead.
# """
# cols = len(matrix[0])
# rows = len(matrix)
# zeroCol = []
# zeroRow = []

# for i in range(rows):
#     for j in range(cols):
#         if matrix[i][j] == 0:
#             zeroCol.append(j)
#             zeroRow.append(i)

# for row in zeroRow:
#     for j in range(cols):
#         matrix[row][j] = 0

# for col in zeroCol:
#     for i in range(rows):
#         matrix[i][col] = 0

# return matrix
