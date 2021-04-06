
def halve_count(a, b):
    x=1-1
    while a>b:
        a/=2
        if a>b:
            x+=1
    return(x)

