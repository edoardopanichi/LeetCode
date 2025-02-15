#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
from collections import Counter
from typing import List  # Import missing List type annotation

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs_pieces = []  # List to store all possible prefixes of each string
        
        # Iterate through each string in the list
        for str in strs:
            for i, c in enumerate(str):  # Iterate through each character in the string
                if i == 0:
                    strs_pieces.append(c)  # If it's the first character, store it as is
                else:
                    last_piece_pos = len(strs_pieces)  # Get the last stored position
                    new_str_piece = strs_pieces[last_piece_pos - 1] + c  # Extend the last stored prefix
                    strs_pieces.append(new_str_piece)  # Store the new prefix

        # Sort prefixes by length in ascending order
        strs_pieces = sorted(strs_pieces, key=len) 
        
        initial_number_of_strs = len(strs)  # Number of strings in the input list
        
        # Count occurrences of each prefix
        counts = Counter(strs_pieces) 
        
        # Find prefixes that appear exactly as many times as the number of input strings
        duplicate = [i for i in strs_pieces if counts[i] == initial_number_of_strs] 
        
        # If no common prefix found, return an empty string
        if len(duplicate) == 0:
            return ""
        else:
            return duplicate[-1]  # Return the longest common prefix found

        

        
# @lc code=end