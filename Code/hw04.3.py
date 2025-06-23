# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1, p2 = headA, headB
        while p1!= p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1
    


# 这里是额外的解法
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        p0 = headA
        while headA:
            headA.val *= -1
            headA = headA.next
        while headB:
            if headB.val < 0:
                while p0:
                    p0.val *= -1
                    p0 = p0.next
                return headB
            headB = headB.next
        while p0:
            p0.val *= -1
            p0 = p0.next
        return None