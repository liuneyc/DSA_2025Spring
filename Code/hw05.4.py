def make(s: str):
    a = []
    sign = '()+-*/'
    tmp = -1
    for i in range(len(s)):
        if s[i] in sign:
            if tmp != -1:
                a.append(s[tmp: i])
                tmp = -1
            a.append(s[i])
        else:
            if tmp == -1:
                tmp = i
    if tmp != -1:
        a.append(s[tmp: len(s)])
    return a

priority = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2
}
for _ in range(int(input())):
    a = make(input())
    # print(a)
    output = []
    operator = []
    for i in a:
        if i not in "()+-*/":
            output.append(i)
        if i == "(":
            operator.append(i)
        if i in priority:
            while operator:
                if operator[-1] == '(':
                    break
                if operator[-1] in priority:
                    if priority[operator[-1]] < priority[i]:
                        break
                output.append(operator.pop())
            operator.append(i)
        if i == ")":
            t = operator.pop()
            while t != '(':
                output.append(t)
                t = operator.pop()
        # print(i, operator, output)

    while operator:
        output.append(operator.pop())
    print(*output)