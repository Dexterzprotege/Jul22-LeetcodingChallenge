# Question: https://leetcode.com/problems/candy/

# Solution:
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        arr = [1 for i in range(n)]
        
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                arr[i] = max(arr[i], arr[i-1] + 1)
        
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                arr[i] = max(arr[i], arr[i+1] + 1)
        
        return sum(arr)
      
# Verdict:
# Runtime: 324 ms, faster than 19.58% of Python3 online submissions for Candy.
# Memory Usage: 16.9 MB, less than 18.08% of Python3 online submissions for Candy.
