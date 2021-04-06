
def maya_number(n):
    if(n==0): return ["@"]
    res=[]
    while(n):
        a=n%20
        n//=20
        now="o"*(a%5)+"-"*(a//5)
        if(now==""): now="@"
        res.append(now)
    return res[::-1]

