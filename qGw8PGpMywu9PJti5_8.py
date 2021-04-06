
def hanoi(n,start = 1,middle = 2,end = 3,ans = None):
    if ans == None:
        ans = []
        if n == 0:
            return []
    if n == 1:
        ans += [(start,end)]
    else:
        hanoi(n-1,start,end,middle,ans)
        ans += [(start,end)]
        hanoi(n-1,middle,start,end,ans)
    return ans

