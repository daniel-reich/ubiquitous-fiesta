
def numbers_need_friends_too(n):
    ans = ""
    n = str(n)
    last = n[0]
    for c in n[1:]:
        if c == last[-1]:
            last += c
        else:
            ans += last if len(last) > 1 else last * 3
            last = c
    ans += last if len(last) > 1 else last * 3
    return int(ans)

