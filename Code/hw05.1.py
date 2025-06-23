# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        a = list1
        b = list2
        if not a:
            return b
        if not b:
            return a
        if a.val < b.val:
            head = a
            a = a.next
        else:
            head = b
            b = b.next
        p = head
        while a and b:
            if a.val < b.val:
                p.next = a
                a = a.next
            else:
                p.next = b
                b = b.next
            p = p.next
        if a:
            p.next = a
        else:
            p.next = b
        return head