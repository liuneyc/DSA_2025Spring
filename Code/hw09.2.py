# Definition for a binary tree node.
from typing import Optional, List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        ans = []
        q = [root]
        cnt = 0
        while q:
            cnt += 1
            t = []
            cur = q[:]
            q = []
            for i in cur:
                t.append(i.val)
                if i.left: q.append(i.left)
                if i.right: q.append(i.right)
            if cnt % 2 == 1:
                ans.append(t)
            else: ans.append(t[::-1])
        return ans
