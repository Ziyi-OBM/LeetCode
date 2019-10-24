# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p=p
        self.q=q
        self.lca=None
        self.isAnces(root)
        return self.lca
    
    def isAnces(self,node):
        if node is None:
            return False
        l=self.isAnces(node.left)
        r=self.isAnces(node.right)
        
        if l and r:
                self.lca=node
                return True
            
        if node.val == self.p.val or node.val == self.q.val:
            if l or r:
                self.lca=node
            return True
        if l or r:
            return True