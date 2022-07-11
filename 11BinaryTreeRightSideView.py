# Question: https://leetcode.com/problems/binary-tree-right-side-view/

# Solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [root]
        while root and stack:
            res.append([node.val for node in stack])
            temp = []
            for node in stack :
                if node.left!=None:
                    temp.append(node.left)
                if node.right!=None:
                    temp.append(node.right)
            stack = temp
        ans = []
        print(res)
        for i in res:
            ans.append(i[-1])
        return ans
      
# Verdict:
# Runtime: 67 ms, faster than 13.37% of Python3 online submissions for Binary Tree Right Side View.
# Memory Usage: 13.6 MB, less than 99.98% of Python3 online submissions for Binary Tree Right Side View.
