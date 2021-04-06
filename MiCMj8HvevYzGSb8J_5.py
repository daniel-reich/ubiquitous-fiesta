
def fibo_word(n):
    x='b' 
    y='a' 
    if n<2:
        return "invalid"
    lst=[]
    lst.append(x)
    lst.append(y)
    for i in range(n-2):
        tmp=y+x 
        lst.append(tmp)
        x=y
        y=tmp
    return ", ".join(lst)

