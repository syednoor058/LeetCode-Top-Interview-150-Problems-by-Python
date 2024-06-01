"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
"""

# Solution:

class Solution:
    def singleNumber(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            nums.sort()
        
            for i in range(len(nums)):
                if nums[i] == nums[i-1] or nums[i] == nums[(i+1)%len(nums)]:
                    continue
                else: return nums[i]