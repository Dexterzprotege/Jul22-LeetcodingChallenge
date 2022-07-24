## Question: https://leetcode.com/problems/search-a-2d-matrix-ii/

# Solution:
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = 0, len(matrix[0])-1
        while row <= len(matrix) - 1 and col >= 0:
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                col -= 1
            else:
                row += 1
        return False
      
# Verdict:
# Runtime: 275 ms, faster than 44.28% of Python3 online submissions for Search a 2D Matrix II.
# Memory Usage: 20.4 MB, less than 84.45% of Python3 online submissions for Search a 2D Matrix II.
