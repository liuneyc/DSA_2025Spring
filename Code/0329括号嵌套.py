class node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        pass

def build(s: str) -> node:
    # print(s[0])
    if s == "*": return None
    if s in "QWERTYUIOPLKJHGFDSAZXCVBNM" and len(s) == 1: return node(s)
    if len(s) == 6: return node(s[0], build(s[2]), build(s[4]))
    tmp = node(s[0])
    cnt = 0
    d = -1
    for i in range(1, len(s)):
        if s[i] == '(': cnt += 1
        if s[i] == ")": cnt -= 1
        if cnt == 1 and s[i] == ",":
            d = i
            break
    # print(f"left= {s[2: d]}")
    tmp.left = build(s[2: d])
    tmp.right = build(s[d+1: -1])
    return tmp
ans = ""
def front(root: node):
    global ans
    ans += root.val
    if root.left: front(root.left)
    if root.right: front(root.right)

def mid(root: node):
    global ans
    if root.left: mid(root.left)
    ans += root.val
    if root.right: mid(root.right)

# r = build("A(B(*,C),D(E,*))")
# front(r)
# print(ans)
# ans = ""
# mid(r)
# print(ans)



for _ in range(int(input())):
    s = input()
    root = build(s)
    ans = ""
    front(root)
    print(ans)
    ans = ""
    mid(root)
    print(ans)
