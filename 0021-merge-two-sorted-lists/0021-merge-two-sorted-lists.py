# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr1 = list1
        curr2 = list2
        
        
        
        result = ListNode()
        curr = result
        # Pointer to the current node in the merged linked list
        
        # Merge the two linked lists while they both have elements
        while curr1 and curr2:
            if curr1.val < curr2.val:
                curr.next = curr1
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr2 = curr2.next
            curr = curr.next
        
        # If there are remaining elements in either of the linked lists, add them to the merged list
        if curr1:
            curr.next = curr1
        if curr2:
            curr.next = curr2
        
        return result.next
                
        