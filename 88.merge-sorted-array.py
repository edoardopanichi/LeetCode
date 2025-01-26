#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
from typing import List

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp_nums1 = nums1[:m]
        solution = temp_nums1 + nums2
        
        num1 = solution 

  
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

s = Solution()  
s.merge(nums1, m, nums2, n)
print(nums1)
# @lc code=end

