
def generate_word(n):  
    if n <= 1:  
        return 'invalid'  
    else:
        res=[]
        x,y='b','a'
        res.append(x)
        for i in range(1,n):
            x,y = y,x+y
            res.append(x)
    return ', '.join(res)

