# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        n, prev, current = None, None, head
        
        
        while current != None:
            
            n = current.next
            current.next = prev
            prev = current
            current = n
        
        return prev
            
            