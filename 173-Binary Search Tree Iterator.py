# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#This problem is basically inorder traversal for BST
class BSTIterator:

    def __init__(self, root: TreeNode):
        import queue
        self.node = root
        self.stack=[]
        if self.node is None:
            return
        self.propLeft()        
        
    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.node = self.stack.pop()
        output=self.node.val
        if self.node.right is not None:            
            self.node=self.node.right
            self.propLeft()
        return output

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """        
        return bool(self.stack)
        
    def propLeft(self):        
        
        while self.node is not None:
            self.stack.append(self.node)
            self.node = self.node.left


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()