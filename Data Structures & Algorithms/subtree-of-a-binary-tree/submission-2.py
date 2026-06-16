# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def identical(root, subRoot):
            p = [(root, subRoot)]
            while p:
                r, sub = p.pop()
                if not r and not sub:
                    continue
                if not r or not sub:
                    return False
                if r.val != sub.val:
                    return False
                else:
                    p.append((r.left, sub.left))
                    p.append((r.right, sub.right))
            return True
        if not root:
            return False
        if not subRoot:
            return True
        s = [root]
        while s:
            curr = s.pop()
            if identical(curr, subRoot):
                return True
            if curr.left:
                s.append(curr.left)
            if curr.right:
                s.append(curr.right)
        return False