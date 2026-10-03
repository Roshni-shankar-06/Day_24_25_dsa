class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        n = len(nums)
        counts = [0] * n
        # Pair each number with its original index to track its position after sorting
        indices = list(enumerate(nums))
        
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            
            return merge(left, right)
        
        def merge(left, right):
            merged = []
            i = j = 0
            right_count = 0  # Tracks how many elements from the right array have been jumped
            
            while i < len(left) and j < len(right):
              
