# Question: https://leetcode.com/problems/wiggle-subsequence/

# Solution:
class Solution:
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []
        for i in range(1, len(nums)):
            if nums[i-1] - nums[i] != 0:
                dp.append(nums[i-1]-nums[i])
        
        if not dp:  return 1
        
        ans = 2
        print(dp)
        for i in range(1, len(dp)):
            if (dp[i-1] > 0 and dp[i] < 0) or (dp[i-1] < 0 and dp[i] > 0):
                ans += 1
        
        return ans
      
# Verdict:
# Runtime: 73 ms, faster than 21.34% of Python3 online submissions for Wiggle Subsequence.
# Memory Usage: 13.9 MB, less than 76.56% of Python3 online submissions for Wiggle Subsequence.
