
def spiral_order(lst):
    v=len(lst)
    h=len(lst[0])
    y=x=k=0
    a=[]
    while k<h*v:        
        while x<h and lst[y][x]!='*':
            a.append(lst[y][x])
            lst[y][x]='*'
            x+=1
            k+=1
        y+=1;x-=1
        while y<v and lst[y][x]!='*':
            a.append(lst[y][x])
            lst[y][x]='*'
            y+=1
            k+=1
        x-=1;y-=1
        while x>=0 and lst[y][x]!='*':
            a.append(lst[y][x])
            lst[y][x]='*'
            x-=1
            k+=1
        x+=1;y-=1
        while y>=0 and lst[y][x]!='*':
            a.append(lst[y][x])
            lst[y][x]='*'
            y-=1
            k+=1
        if lst[y][x]=='*':
            y+=1
            x+=1
    return a

