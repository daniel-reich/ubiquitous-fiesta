
def hanoi(n , fr=1, to=3, tmp=2, ans=None, orig=True):
    if orig:
        ans = []
        if n == 0:
            return ans
    if n == 1:
        ans.append((fr,  to))
        if orig:
            return ans
        else:
            return
    hanoi(n-1, fr, tmp, to, ans, orig=False)
    ans.append((fr, to))
    hanoi(n-1, tmp, to, fr, ans, orig=False)
    if orig:
        return ans

