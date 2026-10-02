class Solution:

  def maxCoins(self, nums: List[int]) -> int:
    nums = [1] + nums + [1]
