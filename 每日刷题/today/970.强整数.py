#
# @lc app=leetcode.cn id=970 lang=python3
# @lcpr version=21907
#
# [970] 强整数
#

# @lc code=start
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:

        res = set()

        v1 = 1 
        for i in range(21):
            v2 = 1 
            for i in range(21):
                v = v1+v2 
                if v <= bound:
                    res.add(v) 
                else:
                    break  
                v2 *= y 
            if v1 > bound:
                break 
            v1 *= x 
        return list(res) 


# @lc code=end



#
# @lcpr case=start
# 2\n3\n10\n
# @lcpr case=end

# @lcpr case=start
# 3\n5\n15\n
# @lcpr case=end

#

