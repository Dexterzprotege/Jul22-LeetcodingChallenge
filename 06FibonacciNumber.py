# Question: https://leetcode.com/problems/fibonacci-number/

# Solution 1: Recursive:
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n-1) + self.fib(n-2)
      
# Verdict:
# Runtime: 1384 ms, faster than 6.90% of Python3 online submissions for Fibonacci Number.
# Memory Usage: 13.9 MB, less than 54.45% of Python3 online submissions for Fibonacci Number.

# Solution 2: Iterative:
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        a, b = 0, 1
        for i in range(2, n+1):
            a, b = b, a + b
        return b
      
# Verdict:
# Runtime: 54 ms, faster than 46.52% of Python3 online submissions for Fibonacci Number.
# Memory Usage: 13.8 MB, less than 95.78% of Python3 online submissions for Fibonacci Number.

# Solution 3: Matrix Exponentiation:
import numpy as np
class Solution:
    def fib(self, n: int) -> int:
        matrix = np.matrix([[1, 1], [1, 0]], dtype=object) ** abs(n)
        if n%2 == 0 and n < 0:
            return -matrix[0,1]
        return matrix[0, 1]

# Verdict:
# Runtime: 225 ms, faster than 28.29% of Python3 online submissions for Fibonacci Number.
# Memory Usage: 31.7 MB, less than 9.50% of Python3 online submissions for Fibonacci Number.

# Solution 4: Binet's Golden Ratio Formula
class Solution:
    def fib(self, n: int) -> int:
        phi = (5**0.5 + 1) / 2
        return round(phi**n / 5**0.5)
      
# Verdict:
# Runtime: 66 ms, faster than 32.70% of Python3 online submissions for Fibonacci Number.
# Memory Usage: 13.7 MB, less than 95.78% of Python3 online submissions for Fibonacci Number.
