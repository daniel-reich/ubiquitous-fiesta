
def check_pattern(c,s):
    dic = dict()
    for i in range(len(s)):
        if s[i] not in dic:
            dic[s[i]] = c[i]
    x = []
    for k in dic.values():
        if k not in x:
            x.append(k)
    if len(x) != len(dic):
        return False
​
    return [dic[k] for k in s] == c

