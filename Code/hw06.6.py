class Node:
    def __init__(self, val=0, key=0, next=None, pre=None):
        self.val = val
        self.key = key
        self.next = next
        self.pre = pre

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.l = 0
        self.dic = {}
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        if key in self.dic:
            self.movetohead(self.dic[key])
            return self.dic[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # print(key, value)
        if key in self.dic:
            self.dic[key].val = value
            self.movetohead(self.dic[key])
            return
        
        if self.l == self.cap:
            # print(self.tail.pre.val)
            self.dic.pop(self.tail.pre.key)
            self.tail.pre = self.tail.pre.pre
            self.tail.pre.next = self.tail

        n = Node(val=value, key=key)
        n.pre = self.head
        n.next = self.head.next
        self.head.next.pre = n
        self.head.next = n
        self.dic[key] = n

        if self.l < self.cap:
            self.l += 1
            return
        
        


    def movetohead(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        node.next = self.head.next
        self.head.next.pre = node
        node.pre = self.head
        self.head.next = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)