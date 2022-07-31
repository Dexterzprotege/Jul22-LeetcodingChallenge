# Question: https://leetcode.com/problems/range-sum-query-mutable/

# Solution:
class NumArray:

    nums = []
    BIT = []
    n = 0
    
    # Reset the BIT
    def init(self, i, val):
        i += 1
        while i <= self.n:
            self.BIT[i] += val
            i += (i & -i)
                
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)
        self.BIT = [0] * (self.n+1)
        for i in range(0, self.n):
            self.init(i, nums[i])
            

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        self.init(index, diff)
        
    def getSum(self, i):
        ans = 0
        i += 1
        while i > 0:
            ans += self.BIT[i]
            i -= (i & -i)
        return ans

    def sumRange(self, left: int, right: int) -> int:
        return self.getSum(right) - self.getSum(left-1)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

# Verdict:
# Runtime: 3268 ms, faster than 50.14% of Python3 online submissions for Range Sum Query - Mutable.
# Memory Usage: 31.1 MB, less than 78.27% of Python3 online submissions for Range Sum Query - Mutable.
