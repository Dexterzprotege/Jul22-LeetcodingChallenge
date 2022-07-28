# Question: https://leetcode.com/problems/valid-anagram/

# Code:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S, T = [0]*26, [0]*26
        for c in s:
            S[ord(c)-ord('a')] += 1
        for c in t:
            T[ord(c)-ord('a')] += 1
        for i in range(26):
            if S[i] != T[i]:
                return False
        return True
      
# Verdict:
# Runtime: 74 ms, faster than 54.74% of Python3 online submissions for Valid Anagram.
# Memory Usage: 14.5 MB, less than 34.60% of Python3 online submissions for Valid Anagram.
