class Solution {
  public int longestValidParentheses(String s) {
    final String s2 = ")" + s;
    // dp[i] := the length of the longest valid parentheses in the substring
    // s2[1..i]
    int dp[] = new int[s2.length()];

 
