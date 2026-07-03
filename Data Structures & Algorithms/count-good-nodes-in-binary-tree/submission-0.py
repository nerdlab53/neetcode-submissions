# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, m):
            c = 0
            if not root:
                return 0
            if root.val >= m:
                c += 1 
            m = max(root.val, m)
            c += dfs(root.left, m)
            c += dfs(root.right, m)
            return c
        return dfs(root, root.val)
