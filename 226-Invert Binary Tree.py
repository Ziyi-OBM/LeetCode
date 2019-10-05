# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#The meme.

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            self.prop(root)        
        return root
        
        
    def prop(self,root):
        if not(root.left is None and root.right is None):
            root.left, root.right = root.right, root.left
            if root.left:
                self.prop(root.left)
            if root.right:
                self.prop(root.right)
