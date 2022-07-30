# Question: https://leetcode.com/problems/word-subsets/

# Solution:
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def counter(word):
            count = [0]*26
            for c in word:
                count[ord(c)-ord('a')] += 1
            return count
        
        count = [0] * 26
        for b in words2:
            tmp = counter(b)
            for i in range(0, 26):
                count[i] = max(count[i], tmp[i])
        
        output = []
        for a in words1:
            tmp = counter(a)
            i = 0
            for i in range(0, 26):
                if tmp[i] < count[i]:
                    break
            if i == 25:
                output.append(a)
        return output
      
# Verdict:
# Runtime: 1750 ms, faster than 24.34% of Python3 online submissions for Word Subsets.
# Memory Usage: 18.6 MB, less than 73.00% of Python3 online submissions for Word Subsets.
