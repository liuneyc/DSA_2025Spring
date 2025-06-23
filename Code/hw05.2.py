# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if head == None: return True
        if head.next == None: return True
        end, mid = head, head
        while end.next:
            if end.next: end = end.next
            else: break
            if mid.next: mid = mid.next
            else: break
            if end.next: end = end.next
            else: break
        print(mid.val)
        
        pre = None
        cur = mid
        while cur is not None:
            forward = cur.next
            cur.next = pre
            pre = cur
            cur = forward

        while pre and head:
            if pre.val != head.val:
                return False
            pre = pre.next
            head = head.next
        return True




