# Question: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# Solution 2:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(root):
            if not root:
                return None
            left = dfs(root.left)
            right = dfs(root.right)
            if root.left:
                left.right = root.right
                root.right = root.left
                root.left = None
            return right or left or root
        dfs(root)
        
# Verdict:
# Runtime: 24 ms, faster than 99.91% of Python3 online submissions for Flatten Binary Tree to Linked List.
# Memory Usage: 15.2 MB, less than 47.67% of Python3 online submissions for Flatten Binary Tree to Linked List.

# --------------------------------------------------------------------------------------------------------------

# Solution 1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        preorder = []
        
        def preOrder(root):
            if root is None:
                return
            preorder.append(root)
            preOrder(root.left)
            preOrder(root.right)
        
        preOrder(root)

        head = root
        for node in preorder[1:]:
            head.left = None
            head.right = node
            head = head.right
            
# Verdict:
# Runtime: 52 ms, faster than 64.64% of Python3 online submissions for Flatten Binary Tree to Linked List.
# Memory Usage: 15.3 MB, less than 47.67% of Python3 online submissions for Flatten Binary Tree to Linked List.
