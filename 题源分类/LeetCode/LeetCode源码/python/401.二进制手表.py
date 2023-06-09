#
# @lc app=leetcode.cn id=401 lang=python3
#
# [401] 二进制手表
#
# https://leetcode-cn.com/problems/binary-watch/description/
#
# algorithms
# Easy (53.37%)
# Likes:    227
# Dislikes: 0
# Total Accepted:    23.9K
# Total Submissions: 44.7K
# Testcase Example:  '0'
#
# 二进制手表顶部有 4 个 LED 代表 小时（0-11），底部的 6 个 LED 代表 分钟（0-59）。
#
# 每个 LED 代表一个 0 或 1，最低位在右侧。
#
#
#
# 例如，上面的二进制手表读取 “3:25”。
#
# 给定一个非负整数 n 代表当前 LED 亮着的数量，返回所有可能的时间。
#
#
#
# 示例：
#
# 输入: n = 1
# 返回: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16",
# "0:32"]
#
#
#
# 提示：
#
#
# 输出的顺序没有要求。
# 小时不会以零开头，比如 “01:00” 是不允许的，应为 “1:00”。
# 分钟必须由两位数组成，可能会以零开头，比如 “10:2” 是无效的，应为 “10:02”。
# 超过表示范围（小时 0-11，分钟 0-59）的数据将会被舍弃，也就是说不会出现 "13:00", "0:61" 等时间。
#
#
#


# @lc code=start
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:

        res = []
        path = []
        for hour in range(12):
            for minute in range(60):
                if bin(hour).count('1') + bin(minute).count('1') == num:
                    res.append(f'{hour}:{minute:02d}')
        return res


# @lc code=end

# def readBinaryWatch(self, num: int) -> List[str]:

#     res = []
#     path = []
#     visited = [0] * 10
#     def backtrack(path):
#         if len(path) == num:
#             hour,minute = 0,0
#             for i in path:
#                 if i < 4:
#                     hour += 2 ** (3-i)
#                 else:
#                     minute += 2 **(9 - i)

#             hour = str(hour) if 0 <= hour <= 11 else None
#             if minute < 59 and minute >= 0:
#                 if minute < 10:
#                     minute = "0" + str(minute)
#                 else:
#                     minute = str(minute)
#             else:
#                 minute = None
#             if hour and minute:
#                 time = hour + ":" + minute
#                 res.append(time) if time not in res else None

#         for idx in range(10):
#             if visited[idx]:
#                 continue
#             path.append(idx)
#             visited[idx] = True
#             backtrack(path)
#             path.pop()
#             visited[idx] = False
#     backtrack(path)
#     return res
