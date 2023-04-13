#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#
# https://leetcode-cn.com/problems/implement-strstr/description/
#
# algorithms
# Easy (39.71%)
# Likes:    835
# Dislikes: 0
# Total Accepted:    354.9K
# Total Submissions: 880.5K
# Testcase Example:  '"hello"\n"ll"'
#
# 实现 strStr() 函数。
#
# 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0
# 开始）。如果不存在，则返回  -1 。
#
#
#
# 说明：
#
# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
#
# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf()
# 定义相符。
#
#
#
# 示例 1：
#
#
# 输入：haystack = "hello", needle = "ll"
# 输出：2
#
#
# 示例 2：
#
#
# 输入：haystack = "aaaaa", needle = "bba"
# 输出：-1
#
#
# 示例 3：
#
#
# 输入：haystack = "", needle = ""
# 输出：0
#
#
#
#
# 提示：
#
#
# 0
# haystack 和 needle 仅由小写英文字符组成
#
#
#


# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:#kmp 
        def getNext(nex,s):
            j = -1 
            nex[0] = j 
            for i in range(1,len(s)):
                while j >= 0 and s[i] != s[j+1]:
                    j = nex[j]
                if s[i] == s[j+1]:
                    j += 1 
                nex[i] = j 
                
        if not needle: 
            return 0 
        n = len(needle)
        h = len(haystack)
        nex = [-1]*n  
        
        getNext(nex,needle)
        
        j = -1 
        for i in range(h):
            while j >= 0 and haystack[i] != needle[j+1]:
                j = nex[j]        
            if haystack[i] == needle[j+1]:
                j += 1 
            
            if j == n - 1:
                return i - n + 1
        return -1 



# @lc code=end
    # def strStr(self, haystack: str, needle: str) -> int:
    #     if not needle:
    #         return 0
    #     for i in range(len(haystack)):
    #         if haystack[i:i+len(needle)] == needle:
    #             return i
    #     return -1

    # def strStr(self, haystack: str, needle: str) -> int:
    #     if not needle:
    #         return 0
    #     for i in range(len(haystack)):
    #         if haystack[i:i+len(needle)] == needle:
    #             return i
    #     return -1
