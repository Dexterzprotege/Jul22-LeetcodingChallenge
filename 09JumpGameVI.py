# Question: https://leetcode.com/problems/jump-game-vi/

# Solution:
class Solution:
    def maxResult(self, nums, k):
        deq, n = deque([0]), len(nums)

        for i in range(1, n):
            while deq and deq[0] < i - k: deq.popleft()
            nums[i] += nums[deq[0]]   
            while deq and nums[i] >= nums[deq[-1]]: deq.pop()
            deq.append(i)
            
        return nums[-1]
      
# Verdict:
# Runtime: 1774 ms, faster than 33.81% of Python3 online submissions for Jump Game VI.
# Memory Usage: 28.2 MB, less than 34.43% of Python3 online submissions for Jump Game VI.
