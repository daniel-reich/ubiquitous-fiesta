
def staircase(n, a=1):
    if n>0 and n>=a: 
        return (n-a)*"_"+a*"#"+("" if n<a+1 else "\n")+staircase(n, a+1)
    if n<0 and abs(n) >= a: 
        return (a-1)*"_"+(abs(n)-a+1)*"#"+("" if abs(n)<a+1 else "\n")+staircase(n,a+1)
    return ""

