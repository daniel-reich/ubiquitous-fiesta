
def is_isomorphic(s, t):
    if type(s) != str or type(t) != str:
        return False
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if s[i] in s[:i]:
            continue
        elif s.count(s[i]) == 1:
            continue
        elif s.count(s[i]) > 1:
             cnt = s.count(s[i]) - 1
             index = s.find(s[i], i + 1, len(s))
             while cnt > 0:
                 if t[index] != t[i]:
                      return False
                 else:
                     cnt -= 1
                     index = s.find(s[i], index +1, len(s))
    for i in range(len(t)):
        if t[i] in t[:i]:
            continue
        elif t.count(t[i]) == 1:
            continue
        elif t.count(t[i]) > 1:
            cnt = t.count(t[i]) - 1
            index = t.find(t[i], i + 1, len(t))
            while cnt > 0:
                if s[index] != s[i]:
                    return False
                else:
                    cnt -= 1
                    index = t.find(t[i], index + 1, len(t))
​
    return True

