"""
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

# Solution:

class Solution:
    def lengthOfLongestSubstring(self, s) -> int:
        unique = set()
        left = 0
        count = 0

        for right in range(len(s)):
            while s[right] in unique:
                unique.remove(s[left])
                left += 1
            unique.add(s[right])
            count = max(count, len(unique))
        
        return count