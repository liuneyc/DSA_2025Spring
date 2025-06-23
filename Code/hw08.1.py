# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def build(a: List[int]):
            n = len(a)
            if n == 1: return TreeNode(a[0])
            if n == 0: return None
            m = n // 2
            return TreeNode(a[m], build(a[0: m]), build(a[m+1:]))
        
        return build(nums)