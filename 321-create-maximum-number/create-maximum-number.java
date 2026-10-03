class Solution {
  public int[] maxNumber(int[] nums1, int[] nums2, int k) {
    int[] ans = new int[k];

    for (int k1 = 0; k1 <= k; ++k1) {
      final int k2 = k - k1;
      if (k1 > nums1.length || k2 > nums2.length)
        continue;
      int[] candidate = merge(maxArray(nums1, k1), maxArray(nums2, k2));
      if (greater(candidate, 0, ans, 0))
        ans = candidate;
    }
   
