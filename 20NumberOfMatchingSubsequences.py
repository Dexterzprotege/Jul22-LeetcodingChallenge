# Question: https://leetcode.com/problems/number-of-matching-subsequences/

# Solution:
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        dic = defaultdict(list)
        
        for word in words:
            dic[word[0]].append(word)
            
        ans = 0
        for c in s:
            char = dic[c]
            dic[c] = []
            
            for word in char:
                if len(word) == 1:
                    ans += 1
                else:
                    dic[word[1]].append(word[1:])
        return ans
      
# Verdict:
# Runtime: 685 ms, faster than 60.94% of Python3 online submissions for Number of Matching Subsequences.
# Memory Usage: 15.6 MB, less than 51.10% of Python3 online submissions for Number of Matching Subsequences.
