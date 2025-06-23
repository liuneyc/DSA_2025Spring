class Node:
    def __init__(self, val = "", next = None, pre = None):
        self.val = val
        self.next = next
        self.pre = pre

class BrowserHistory:

    def __init__(self, homepage: str):
        self.root = Node(val=homepage)
        self.now = self.root

    def visit(self, url: str) -> None:
        now = Node(val=url, pre=self.now)
        self.now.next = now
        self.now = now
        pass

    def back(self, steps: int) -> str:
        while steps > 0:
            if self.now.pre == None:
                return self.now.val
            self.now = self.now.pre
            steps -= 1
        return self.now.val

    def forward(self, steps: int) -> str:
        while steps > 0:
            if self.now.next == None:
                return self.now.val
            self.now = self.now.next
            steps -= 1
        return self.now.val
        pass


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)