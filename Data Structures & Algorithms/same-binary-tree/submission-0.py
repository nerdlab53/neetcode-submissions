# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        stack1 = [p]
        stack2 = [q]
        while stack1 and stack2:
            curr1 = stack1.pop()
            curr2 = stack2.pop()
            if curr1.val != curr2.val:
                return False
            
            if curr1.left and curr2.left:
                stack1.append(curr1.left)
                stack2.append(curr2.left)
            elif curr1.left or curr2.left:
                return False
            
            if curr1.right and curr2.right:
                stack1.append(curr1.right)
                stack2.append(curr2.right)
            elif curr2.right or curr2.right:
                return False
        return len(stack1) == len(stack2)
            
