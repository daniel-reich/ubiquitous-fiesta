
def ping_pong(lst, key):
    ans = []
    if key == True:
        for i in lst:
            ans.append(i)
            ans.append('Pong!')
        return (ans)
    else:
        for i in lst:
            ans.append(i)
            ans.append('Pong!')
        return (ans[:-1])

