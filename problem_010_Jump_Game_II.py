"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
"""

# Solution:

class Solution:
    def jump(self, nums) -> int:
        left_pointer = 0
        right_pointer = 0
        jump_count = 0

        while right_pointer < len(nums) - 1:
            max_jump_index = 0
            for i in range(left_pointer, right_pointer+1):
                max_jump_index = max(max_jump_index, i+nums[i])
            left_pointer = right_pointer
            right_pointer = max_jump_index
            jump_count += 1
        
        return jump_count

        
    
        return jump_count