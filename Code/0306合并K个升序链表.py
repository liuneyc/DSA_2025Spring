# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def twolist(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1, h2 = l1, l2
        head, tail = None, None
        if h1.val < h2.val:
            head = h1
            tail = h1
            h1 = h1.next
        else:
            head = h2
            tail = h2
            h2 = h2.next
        while h1 and h2:
            if h1.val < h2.val:
                tail.next = h1
                h1 = h1.next
            else:
                tail.next = h2
                h2 = h2.next
            tail = tail.next
        if h1 != None: tail.next = h1
        else: tail.next = h2
        return head


    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        valid_lists = [l for l in lists if l is not None]
        n = len(valid_lists)
        print(n)
        if n == 0: return None
        if n == 1: return valid_lists[0]
        head = valid_lists[0]
        for i in range(1, n):
            head = self.twolist(head, valid_lists[i])
        return head
        