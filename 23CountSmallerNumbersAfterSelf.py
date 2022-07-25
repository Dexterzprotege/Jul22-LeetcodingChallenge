# Question: https://leetcode.com/problems/count-of-smaller-numbers-after-self/

# Solution:
from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums):
        sortedList = SortedList()
        ans = []
        
        for num in nums[::-1]:
            pos = SortedList.bisect_left(sortedList, num)
            ans.append(pos)
            sortedList.add(num)
        
        return ans[::-1]
      
# Verdict:
# Runtime: 3499 ms, faster than 69.66% of Python3 online submissions for Count of Smaller Numbers After Self.
# Memory Usage: 33.7 MB, less than 64.40% of Python3 online submissions for Count of Smaller Numbers After Self.
