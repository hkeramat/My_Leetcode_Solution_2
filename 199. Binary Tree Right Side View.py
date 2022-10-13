# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        
        level = 0
        levels =[]
        
        q = collections.deque([root])
        
        while q:
            levels.append([])
            
            
            for i in range(len(q)):
                
                cur = q.popleft()
                levels[level].append(cur.val)
            
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            level += 1
        return [levels[x][-1] for x in range( level)]
