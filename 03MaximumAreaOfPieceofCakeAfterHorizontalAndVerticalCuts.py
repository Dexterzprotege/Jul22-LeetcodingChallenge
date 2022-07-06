# Question: https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

# Solution: Sort and compare:
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts = [0] + sorted(horizontalCuts) + [h]
        verticalCuts = [0] + sorted(verticalCuts) + [w]
        
        width, height = 0, 0
        
        for i in range(1, len(horizontalCuts)):
            width = max(width, abs(horizontalCuts[i] - horizontalCuts[i-1]))
        for i in range(1, len(verticalCuts)):
            height = max(height, abs(verticalCuts[i] - verticalCuts[i-1]))
        
        return (width * height) % (10**9 + 7)
      
# Verdict:
# Runtime: 565 ms, faster than 26.80% of Python3 online submissions for Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts.
# Memory Usage: 28.3 MB, less than 30.77% of Python3 online submissions for Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts.
