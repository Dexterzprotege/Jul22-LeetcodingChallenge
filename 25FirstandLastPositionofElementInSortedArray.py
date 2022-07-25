# Question: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# Solution:
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binSearch(bias):
            left, right = 0, len(nums) - 1
            i = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    i = mid
                    if bias:
                        right = mid - 1
                    else:
                        left = mid + 1
            return i
        return [binSearch(True), binSearch(False)]
                    
# Verdict:
# Runtime: 126 ms, faster than 54.16% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
# Memory Usage: 15.5 MB, less than 10.25% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
