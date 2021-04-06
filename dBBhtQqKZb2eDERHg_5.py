
def numberSequence(n, d = 1, ans = ''):
    if n <= 0: return '-1'
    if d == 1:
        ans = '1' if n%2 else '1 1'
    else:
        ans = str(d) + ' ' + ans + ' ' + str(d)
    return ans if n == (len(ans) + 1)//2 else numberSequence(n, d + 1, ans)

