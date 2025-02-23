# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        current = dummy
        current_1 = list1
        current_2 = list2

        # get the 2 current values
        # if value is less than or equal
        if list1 == None:
            return list2
        elif list2 == None:
            return list1

        while current_1 and current_2:
            if current_1.val <= current_2.val:
                current.next = current_1
                current_1 = current_1.next
            else:
                current.next = current_2
                current_2 = current_2.next
            current = current.next
        # add to tail of list
        if current_1 != None:
            current.next = current_1
        elif current_2 != None:
            current.next = current_2

        return dummy.next