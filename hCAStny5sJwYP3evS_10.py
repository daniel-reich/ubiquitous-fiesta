
def is_early_bird(_range, n):
    x,y=[],[]
    n=str(n)
    for i in range(0,_range+1):
        x.append(i)
    x=[str(i)for i in x]    
    res=''.join(x)
    for i in range(len(res)-1):
        if len(n)==2:
            if res[i]==str(n[0]) and res[i+1]==str(n[1]):
                y.append([i,i+1])
        if len(n)==3:
            if res[i]==str(n[0]) and res[i+1]==str(n[1]) and res[i+2]==str(n[2]):
                y.append([i,i+1,i+2])      
    if len(y)==1:
        return y
    else:
        y= y+['Early Bird!']
        return y

