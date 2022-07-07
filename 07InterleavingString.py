# Question: https://leetcode.com/problems/interleaving-string/

# Solution:
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        row, col, n = len(s1), len(s2), len(s3)
        
        if row + col != n:
            return False
        
        dp = [[False for i in range(col+1)] for j in range(row+1)]
        
        dp[0][0] = True
        for i in range(1, row + 1):
            if s1[i-1] == s3[i-1]:
                dp[i][0] = dp[i-1][0]
            else:
                dp[i][0] = False
        
        for j in range(1, col + 1):
            if s2[j-1] == s3[j-1]:
                dp[0][j] = dp[0][j-1]
            else:
                dp[0][j] = False
                
        for i in range(1, row+1):
            for j in range(1, col+1):
                if s1[i-1] == s3[i+j-1]:
                    dp[i][j] = dp[i-1][j]
                if s2[j-1] == s3[i+j-1]:
                    dp[i][j] = dp[i][j] or dp[i][j-1]
        print(dp)
        
        return dp[-1][-1]

# Verdict:
# Runtime: 77 ms, faster than 33.02% of Python3 online submissions for Interleaving String.
# Memory Usage: 14.4 MB, less than 51.18% of Python3 online submissions for Interleaving String.
