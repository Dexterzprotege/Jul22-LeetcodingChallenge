class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        perimeter = sum(matchsticks)
        length = perimeter // 4
        sides = [0] * 4
        if perimeter % 4 != 0:
            return False
        matchsticks.sort(reverse=True)

        def backtrack(i):
            if i == len(matchsticks):
                return True
            
            for j in range(4):
                if sides[j] + matchsticks[i] <= length:
                    sides[j] += matchsticks[i]
                    if backtrack(i+1):
                        return True
                    sides[j] -= matchsticks[i]
            return False
        return backtrack(0)
        
  class Solution:
    def makesquare(self, nums):
        N = len(nums)
        basket, rem = divmod(sum(nums), 4)
        if rem or max(nums) > basket: return False
        
        @lru_cache(None)
        def dfs(mask):
            if mask == 0: return 0
            for j in range(N):
                if mask & 1<<j:
                    neib = dfs(mask ^ 1<<j)
                    if neib >= 0 and neib + nums[j] <= basket:
                        return (neib + nums[j]) % basket
            return -1
                    
        return dfs((1<<N) - 1) == 0
