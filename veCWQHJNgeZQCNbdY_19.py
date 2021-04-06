
def root_digit(n):
    l=[int(i) for i in str(n)]
    s=sum(l)
    if(len(str(s))>1):
​
        return root_digit(s)
    return s

