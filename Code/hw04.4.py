# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        a = None
        while head:
            if not a:
                a = ListNode(head.val)
            else:
                b = ListNode(head.val)
                b.next = a
                a = b
            head = head.next
        return a
