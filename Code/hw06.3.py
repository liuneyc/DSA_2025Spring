from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root == None:
            return ans

        def dfs(root: Optional[TreeNode]):
            if root.left != None:
                dfs(root.left)
            
            ans.append(root.val)
            if root.right != None:
                dfs(root.right)
        
        dfs(root)
        return ans
            