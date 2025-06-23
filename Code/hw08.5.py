class node:
    def __init__(self, val, son=None):
        self.val = val
        self.son = [] if son == None else son
        self.soncnt = len(self.son)

    def adson(self, root):
        self.son.append(root)
        self.soncnt += 1
    

def build(s):
    # print(s)
    if len(s) == 1 and s in "QWERTYUIOPLKJHGFDSAZXCVBNM": return node(s)
    if len(s) == 4: return node(s[0], [node(s[2])])
    tmp = node(s[0])
    l = len(s)
    i = 1
    cnt = 0
    cur = 2
    while i < l:
        if s[i] == "(": cnt += 1
        if s[i] == ')': cnt -= 1
        if cnt == 1 and s[i] == ",":
            tmp.adson(build(s[cur: i]))
            cur = i+1
        i += 1
    tmp.adson(build(s[cur: l-1]))
    return tmp

root = build(input())

ans = ""
def front(root: node):
    global ans
    ans += root.val
    for i in root.son: front(i)

def back(root: node):
    global ans
    for i in root.son: back(i)
    ans += root.val


front(root)
print(ans)
ans = ''
back(root)
print(ans)
