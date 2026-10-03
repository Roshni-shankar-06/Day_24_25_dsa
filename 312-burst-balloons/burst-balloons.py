class Solution:

  def maxCoins(self, nums: List[int]) -> int:
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]

   
