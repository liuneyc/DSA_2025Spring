# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def count(root: Optional[TreeNode]) -> int:
            l = 0
            tmp = root
            while tmp:
                l += 1
                tmp = tmp.left
            return l
        if not root: return 0
        l, r = count(root.left), count(root.right)
        if l == r: return (1<<l) + self.countNodes(root.right)
        if l != r: return (1<<r) + self.countNodes(root.left)