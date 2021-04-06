
def news_at_ten(txt, n):
    txt += ' ' * n
    txt = [t for t in txt]
    ans = []
    cur = ' ' * n
    ans.append(cur)
    while len(txt) > 0:
        cur = cur[1:] + txt.pop(0)
        ans.append(cur)
    return ans

