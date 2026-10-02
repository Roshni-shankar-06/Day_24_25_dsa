class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def backtrack(open_count, close_count, s):
            if len(s) == 2 * n:
                res.append(s)
                return

            if open_count < n:
                backtrack(open_count + 1, close_count, s + "(")
