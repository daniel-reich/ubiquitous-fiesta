
def look_and_say(n):
    l = str(n)
    if len(l)%2 !=0 :return 'invalid'
    res =[]
    for i in range(0,len(l),2):
        ans =l[i:i+2]
        ans = ans[1]*int(ans[0]) if int(ans[0])!=0 else ''
        res.append(ans)
    return  int(''.join(res))

