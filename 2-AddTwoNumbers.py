#Definition for singly-linked list.
#class ListNode:
#    def __init__(self, x):
#        self.val = x 
#        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        indent = 0
        headPtr = result = ListNode(0)
        
        while l1 != None and l2 != None:
            
            added = l1.val + l2.val + indent
            indent = 0
            result.next = ListNode(added%10)
            if added/10>=1:
                indent = 1

            l1 = l1.next
            l2 = l2.next
            result = result.next
  
        while l1 != None:
            added = l1.val+indent
            indent = 0
            result.next = ListNode(added%10)
            if added/10>=1:
                indent = 1
            l1 = l1.next
            result = result.next    
            
        while l2 != None:
            added = l2.val+indent
            indent = 0
            result.next = ListNode(added%10)
            if added/10>=1:
                indent = 1
            l2 = l2.next
            result = result.next    
   
        if indent != 0:
                result.next=ListNode(1)
                indent = 0  
            
        return headPtr.next