# Comments below are added by ChatGPT to improve code clarity.

#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start


class Solution:
    def twoSum_mine(self, nums: List[int], target: int) -> List[int]:
        og_nums = nums.copy()  # Copy the original list to preserve the order.
        nums.sort()  # Sort the list to facilitate pair searching.
        # print(nums)  # Debugging: Show sorted numbers.

        # Variable to store the pair of numbers that sum to the target.
        values = None
        for idx, num in enumerate(nums):  # Iterate over sorted numbers.
            if values != None:  # Break early if the pair is found.
                break
            else:
                # Iterate over potential pair elements.
                for i in range(1, len(nums)-idx):
                    # print(f"num is {num} and nums[idx+i] is {nums[idx+i]}")  # Debugging: Show current numbers.
                    # Check if the pair sums to the target.
                    if (num + nums[idx+i]) == target:
                        # Store the pair of values.
                        values = [num, nums[idx+i]]
                        break  # Exit inner loop once the pair is found.
                    # Exit loop early if sum exceeds target.
                    if (num + nums[idx+i]) > target:
                       break

        # Find the indices of the pair in the original list.
        first_index = og_nums.index(values[0])
        possible_second_index = [
            i for i, x in enumerate(og_nums) if x == values[1]
        ]
        # Remove first_index from possible_second_index if it's present.
        if first_index in possible_second_index:
            possible_second_index.remove(first_index)
            # print(possible_second_index)  # Debugging: Show possible indices.

        # Take the first remaining index.
        second_index = possible_second_index[0]

        # print(possible_second_index)  # Debugging: Show possible second indices.
        indices = [first_index, second_index]  # Construct the indices list.
        # print(og_nums)  # Debugging: Show original list.
        # print(indices)  # Debugging: Show final indices.

        return indices  # Return the indices of the two numbers.

# @lc code=end
