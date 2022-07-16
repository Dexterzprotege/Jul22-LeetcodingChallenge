# Question: https://leetcode.com/problems/out-of-boundary-paths/

# Solution:
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, i: int, j: int) -> int:
        dic = {}
        def rec(row, col, maxMove):
            if (row, col, maxMove) in dic:
                return dic[(row, col, maxMove)]
            if row < 0 or col < 0 or row >= m or col >= n:
                return 1
            if maxMove == 0:
                return 0
            ans = 0
            for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ans += rec(row + x, col + y, maxMove - 1)
            dic[(row, col, maxMove)] = ans
            return ans
        return rec(i, j, maxMove) % (10**9+7)
        
        
# Verdict:
# Runtime: 125 ms, faster than 87.47% of Python3 online submissions for Out of Boundary Paths.
# Memory Usage: 18.2 MB, less than 50.89% of Python3 online submissions for Out of Boundary Paths.
