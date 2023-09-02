# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        slow = head
        fast = head.next
        
        # find midpoint
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            
        # reverse second half
        tail = slow.next
        prev = None
        slow.next = None
        
        while tail:
            temp = tail.next
            tail.next = prev
            prev = tail
            tail = temp
        
        first_half, second_half = head, prev
        while second_half:
            temp1 = first_half.next
            temp2 = second_half.next
            
            first_half.next = second_half
            second_half.next = temp1
            
            first_half, second_half = temp1, temp2
            