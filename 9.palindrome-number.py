#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start

# Done without converting to a string

import math
class Solution:
    
    def getDigit(self, x:int, n:int) -> int:
        # n = 0 extract the right most digit
        
        # First dividing (//) by 10**n we get the integer part only. Notice that dividing 10**n
        # moves the comma of the number by n position. e.g. x=65421 x/10**3 = 65,421. But since we
        # use // we remain with 65.
        quotient = x // 10**n 
        # The Modulus Operator applied in combination with 10, returns the digit after the comma if
        # you were to perform a division by 10. E.g. 65/10 = 6.5, hence we would get 5. 
        digit_n = quotient % 10
        
        return digit_n

    def totalNumberOfDigits(self, x:int) -> int:
        # x must be non-negative
        if x == 0:
            number_of_digits = 1
        else:
            # e.g. for a number with three digits (i.e. < 1000) the solution is alway 2.xxx, because
            # 10^3 is already bigger.
            number_of_digits = int(math.log10(x))+1
        
        return number_of_digits
    
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            number_of_digits = self.totalNumberOfDigits(x)
            # print(f"number of digits {number_of_digits}")
            all_digits_are_equal = True
            
            # We check ony the first half of the number
            for i in range(int(number_of_digits/2)):
                left_digit = self.getDigit(x, i)
                # print(f"\nleft digit {left_digit}")
                right_digit = self.getDigit(x, number_of_digits-i-1)
                # print(f"right digit {right_digit}")
                if left_digit == right_digit:
                    continue
                else:
                    all_digits_are_equal = False
                    break
            solution = True * all_digits_are_equal
        else:
            solution = False
            
        return bool(solution)
            
        
# @lc code=end

