class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2 = 0  # max money from 2 houses ago
        prev1 = 0  # max money from 1 house ago
        
        for num in nums:
            
