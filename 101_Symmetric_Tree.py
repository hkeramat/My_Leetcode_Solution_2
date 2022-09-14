# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isSymmetric(self, root) :
        #The number of nodes in the tree is in the range [1, 1000]
        return self.isMirror(root.left, root.right)
    
    
    def isMirror(self, right, left):
        if not right and not left: return True
        if not right or not left: return False
        return right.val == left.val and self.isMirror(right.right, left.left) and self.isMirror(right.left, left.right)
