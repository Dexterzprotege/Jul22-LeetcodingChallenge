# Question: https://leetcode.com/problems/find-and-replace-pattern/

# Solution:
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def normalise(w):
            dic = {}
            output = []
            i = 0
            for c in w:
                if c not in dic:
                    i += 1
                    dic[c] = i
                output.append(dic[c])
            return output
        
        res = []
        p = normalise(pattern)
        for w in words:
            if normalise(w) == p:
                res.append(w)

        return res
      
# Verdict:
# Runtime: 60 ms, faster than 29.41% of Python3 online submissions for Find and Replace Pattern.
# Memory Usage: 13.9 MB, less than 76.64% of Python3 online submissions for Find and Replace Pattern.
