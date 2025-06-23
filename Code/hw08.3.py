# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        if root == None: return 0
        def dfs(root: Optional[TreeNode], s: int):
            nonlocal ans
            if root.left == None and root.right == None: ans += s
            if root.left: dfs(root.left, s * 10 + root.left.val)
            if root.right: dfs(root.right, s * 10 + root.right.val)
        
        dfs(root, root.val)
        return ans