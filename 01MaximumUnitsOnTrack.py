# Question: https://leetcode.com/problems/maximum-units-on-a-truck/

# Solution 1: Reverse sort and count
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key = lambda x: x[1], reverse = True)
        ans = 0
        for box, unit in boxTypes:
            if truckSize >= box:
                ans += box * unit
                truckSize -= box
            else:
                ans += truckSize * unit
                return ans
        return ans

# Verdict:
# Runtime: 164 ms, faster than 91.66% of Python3 online submissions for Maximum Units on a Truck.
# Memory Usage: 14.3 MB, less than 83.07% of Python3 online submissions for Maximum Units on a Truck.

# Solution 2: Bucket sort
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        buckets = [-1] * 1001
        for box, unit in boxTypes:
            if buckets[unit] == -1:
                buckets[unit] = box
            else:
                buckets[unit] += box
        ans = 0
        for i in range(1000, -1, -1):
            if buckets[i] == -1:
                continue
            if buckets[i] <= truckSize:
                ans += buckets[i] * i
                truckSize -= buckets[i]
            else:
                ans += truckSize * i
                return ans
        return ans

# Verdict:
# Runtime: 283 ms, faster than 30.89% of Python3 online submissions for Maximum Units on a Truck.
# Memory Usage: 14.4 MB, less than 83.07% of Python3 online submissions for Maximum Units on a Truck.
