# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        current = dummy

        # get the 2 current values
        # if value is less than or equal
        # if list1 == None:
        #     return list2
        # elif list2 == None:
        #     return list1

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        # add to tail of list
        if list1 != None:
            current.next = list1
        elif list2 != None:
            current.next = list2

        return dummy.next