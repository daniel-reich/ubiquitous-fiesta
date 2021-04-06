
def expand_front(n):
    s = str(n)
    p = 10**(len(s) - 1)
    ans = str(int(s[0]) * p)
    p //= 10
    for d in s[1:]:
        if d != '0':
            ans += " + " + str(int(d) * p)
        p //= 10
    return ans
​
def expand_back(n):
    ans = ""
    p = 1
    for d in n:
        p *= 10
        if d != '0':
            ans += " + " + d + "/" + str(p)
    return ans
​
def expanded_form(num):
    ans = expand_front(int(num))
    if num != int(num):
        ans += expand_back(str(num).split('.')[1])
    if ans[:4] == "0 + ":
        ans = ans[4:]
    return ans

