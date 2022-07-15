# Question: https://leetcode.com/problems/max-area-of-island/

# Solution:
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        count, n, m = 0, len(grid), len(grid[0])
        
        # Depth First Search in all 4 directions
        def dfs(i, j):
            if i < 0 or i == n or j < 0 or j == m or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return 1 + dfs(i+1, j) + dfs(i, j+1) + dfs(i-1, j) + dfs(i, j-1)
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    count = max(count, dfs(i, j))
        return count
      
# Verdict:
# Runtime: 299 ms, faster than 14.24% of Python3 online submissions for Max Area of Island.
# Memory Usage: 16.5 MB, less than 69.88% of Python3 online submissions for Max Area of Island.
