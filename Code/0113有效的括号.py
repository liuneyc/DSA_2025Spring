class Solution:
    def isValid(self, s: str) -> bool:
        b, m, small, a = 0, 0, 0, []
        for i in s:
            if i == '(':
                small += 1
                a.append(i)
            if i == '[':
                m += 1
                a.append(i)
            if i == '{':
                b += 1
                a.append(i)
            if i == ')':
                if a[-1] != '(':
                    return False
                else:
                    a.pop()
                    small -= 1
            if i == ']':
                if a[-1] != '[':
                    return False
                else:
                    a.pop()
                    m -= 1
            if i == '}':
                if a[-1] != '{':
                    return False
                else:
                    a.pop()
                    b -= 1
        if small == b == m == 0:
            return True
        else:
            return False
            