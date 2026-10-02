class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2 = 0  # max money from 2 houses ago
        prev1 = 0  # max money from 1 house ago
        
        for num in nums:
            current = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = current
            
        return prev1

