"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

# Solution:

class Solution:
    def majorityElement(self, nums) -> int:
        
        nums.sort()
        
        pointer = 0
        max_count = 0
        var = 0
        
        while pointer < len(nums):
            count = 0
            for i in range (pointer, len(nums)):
                if nums[pointer] == nums [i]:
                    count += 1
                    pointer = i
                else:
                    break
            
            if count > max_count:
                max_count = count
                var = nums[pointer]
            
            pointer += 1
            
        return var