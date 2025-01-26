#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        # x % 10 returns the last digit of x
        reversed = 0 
        iter = 0
        
        while x > 0:
            # at the first iteration we only add the last digit, but we actually want this to be the 
            # first digit, so at every iteration we multiply it by 10 to increase its digit position 
            # by 1.
            reversed = 10*reversed + (x % 10)
            x = x // 10
        if x < 0:
            x = -x
            while x > 0:
                reversed = 10*reversed + (x % 10)
                x = x // 10
            reversed *= -1
            
        if reversed > (2**31 - 1) or reversed < (-2**31):
            reversed = 0
        return reversed
        
# @lc code=end

