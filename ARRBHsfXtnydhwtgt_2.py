
def compress(c, ans=""):
    if len(c) == 0:
        return ans
        ans += last
        if cnt > 1:
            ans += str(cnt)
        return ans
    cur = c.pop(0)
    cnt = 1
    while len(c) > 0 and c[0] == cur:
        c.pop(0)
        cnt += 1
    ans += cur
    if cnt > 1:
        ans += str(cnt)
    return compress(c, ans)

