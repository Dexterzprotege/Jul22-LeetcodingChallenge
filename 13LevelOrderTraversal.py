# Question: https://leetcode.com/problems/binary-tree-level-order-traversal/

# Solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
        return res
      
# Verdict:
# Runtime: 44 ms, faster than 74.01% of Python3 online submissions for Binary Tree Level Order Traversal.
# Memory Usage: 14.3 MB, less than 51.36% of Python3 online submissions for Binary Tree Level Order Traversal.
