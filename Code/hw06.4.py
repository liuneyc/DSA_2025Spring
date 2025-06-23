from typing import Optional, List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        ans = []
        tmp = []
        a = deque([(root, 0)])
        dd = 0
        while a:
            t = a.popleft()
            r0 = t[0]
            d0 = t[1]
            if d0 != dd:
                ans.append(tmp)
                tmp = [r0.val]
                dd = d0
            else:
                tmp.append(r0.val)
            d1 = d0 + 1
            if r0.left != None:
                r1 = r0.left
                a.append((r1, d1))
            if r0.right != None:
                r2 = r0.right
                a.append((r2, d1))
        ans.append(tmp)
        return ans