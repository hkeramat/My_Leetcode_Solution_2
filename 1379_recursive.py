# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self,o,c, target):
        def inorder(o,c):
            if o:
                inorder(o.left, c.left)

                if o is target:
                    return c

            inorder(o.right, c.right)

        inorder(o,c)

        return c



