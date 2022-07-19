# Question: https://leetcode.com/problems/pascals-triangle/

# Solution:
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(1, numRows):
            ans.append(ans[-1] + [1])
            ans[i][0] = ans[i][-1] = 1
            for j in range(1, i):
                ans[i][j] = ans[i-1][j-1] + ans[i-1][j]
        return ans
        
# Verdict:
# Runtime: 37 ms, faster than 81.15% of Python3 online submissions for Pascal's Triangle.
# Memory Usage: 13.8 MB, less than 66.48% of Python3 online submissions for Pascal's Triangle.
