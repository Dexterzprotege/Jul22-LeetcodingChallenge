# Question: https://leetcode.com/problems/longest-consecutive-sequence/

# Solution 1: Sorting and calculating
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(nums)
        ans, temp = 1, 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] - nums[i-1] == 1:
                temp += 1
            else:
                ans = max(ans, temp)
                temp = 1
        return max(ans, temp)

# Verdict:
# Runtime: 600 ms, faster than 53.46% of Python3 online submissions for Longest Consecutive Sequence.
# Memory Usage: 26.9 MB, less than 91.49% of Python3 online submissions for Longest Consecutive Sequence.

# Solution 2: Sets and calculating
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        for n in nums:
            if n-1 not in nums:
                m = n + 1
                while m in nums:
                    m += 1
                ans = max(ans, m - n)
        return ans
      
# Verdict:
# Runtime: 487 ms, faster than 67.41% of Python3 online submissions for Longest Consecutive Sequence.
# Memory Usage: 28 MB, less than 72.70% of Python3 online submissions for Longest Consecutive Sequence.
