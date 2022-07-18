# Question: https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

# Solution:
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n, m = len(matrix[0]), len(matrix)
        ans = 0
        
        for row in matrix:
            for j in range(1, len(row)):
                row[j] += row[j-1]
                
        for i in range(n):
            for j in range(i, n):
                dic = defaultdict(int)
                cumsum = 0
                dic[0] = 1
                
                for k in range(m):
                    if i != 0:
                        cumsum += matrix[k][j] - matrix[k][i-1]
                    else:
                        cumsum += matrix[k][j]
                    if cumsum - target in dic:
                        ans += dic[cumsum-target]
                    dic[cumsum] += 1
        
        return ans
      
# Verdict:
# Runtime: 1373 ms, faster than 52.14% of Python3 online submissions for Number of Submatrices That Sum to Target.
# Memory Usage: 15 MB, less than 21.80% of Python3 online submissions for Number of Submatrices That Sum to Target.
