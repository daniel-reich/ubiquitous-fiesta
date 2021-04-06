
def stmid(string):
    ans = ''
    for x in string.split():
        if len(x) % 2 == 0:
            ans += x[0]
        else:
            ans += x[len(x)//2]
    return ans

