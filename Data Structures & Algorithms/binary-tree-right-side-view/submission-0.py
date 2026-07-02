# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        from collections import deque
        q = deque()
        q.append(root)
        while q:
            _l = len(q)
            for i in range(_l):
                c = q.popleft()
                if i == _l-1:
                    res.append(c.val)                
                if c.left:
                    q.append(c.left)
                if c.right:
                    q.append(c.right)
        return res