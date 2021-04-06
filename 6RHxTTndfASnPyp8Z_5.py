
def compress(chars):
    last = chars[0]
    cnt = 1
    ans = ""
    for cur in chars[1:]:
        if cur == last:
            cnt += 1
        else:
            ans += last
            if cnt > 1:
                ans += str(cnt)
            last = cur
            cnt = 1
    ans += last
    if cnt > 1:
        ans += str(cnt)
    return ans

