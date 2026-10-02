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
                # If the element in the right array is smaller
                if right[j][1] < left[i][1]:
                    merged.append(right[j])
                    right_count += 1
                    j += 1
                else:
                    # The element in the left array is smaller or equal
                    # Add the accumulated right_count to this element's original index
                    counts[left[i][0]] += right_count
                    merged.append(left[i])
                    i += 1
            
            # Append remaining elements
            while i < len(left):
                counts[left[i][0]] += right_count
                merged.append(left[i])
                i += 1
                
            while j < len(right):
                merged.append(right[j])
                j += 1
                
         
