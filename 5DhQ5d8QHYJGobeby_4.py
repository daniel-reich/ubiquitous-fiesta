
def hot_brick(t):
    brick=[[25 for x in range(10)] for y in range(10)]  
    brick[9]=[90 for x in range(10)]
    d=((0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1))    
    for minutes in range(t):
        temp=[[0 for x in range(10)] for y in range(10)]
        temp[9]=[90 for x in range(10)]
        for m in range(9):
            for i in range(10):
                s=brick[m][i]
                for p in range(8):
                    y=m+d[p][1]
                    x=i+d[p][0]
                    if x<0 or x>9 or y<0:
                        s+=25
                    else:
                        s+=brick[y][x]
                temp[m][i]=round(s/9)
        brick=temp.copy()
    return brick

