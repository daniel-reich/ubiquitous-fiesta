
def super_digit(n, k):
    res,sum='',0
    for i in range(k):
        res+=str(n)   
    if len(res)>1:
        for i in res:
            sum+=int(i)  
    a=str(sum)
    if len(a)==3:        
        return int(a[0])+int(a[1])+int(a[2])           
    c=str(int(a[0])+int(a[1])) 
    if len(c)==2:
        return int(c[0])+int(c[1])
    else:
        return int(c)

