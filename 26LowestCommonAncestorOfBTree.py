# Question: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Code:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root is p or root is q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right
      
# Verdict:
# Runtime: 129 ms, faster than 30.05% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
# Memory Usage: 26.2 MB, less than 61.82% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
