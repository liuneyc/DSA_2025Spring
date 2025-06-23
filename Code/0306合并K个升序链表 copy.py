# Definition for singly-linked list.
from typing import Optional, List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        a = []
        if len(lists) == 0:
            return None
        for i in lists:
            if i == None:
                continue
            while i:
                a.append(i.val)
                i = i.next
                print(a)
        a.sort()
        print(a)
        if len(a) == 0:
            return None
        if len(a) == 1:
            return ListNode(a[0])
        head = ListNode(a[0])
        tail = head
        for i in a[1:]:
            tail.next = ListNode(i)
            tail = tail.next
        # while head:
        #     print(head.val, end=" -> " if head.next else "\n")
        #     head = head.next
        return head