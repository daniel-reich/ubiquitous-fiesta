
def crop_hydrated(field):
    v0=len(field);h0=len(field[0])
    d=((0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1))    
    for v in range(v0):
        for h in range(h0):
            if field[v][h]=='c':
                count=0
                for p in range(8):
                    y=v+d[p][1]
                    x=h+d[p][0]
                    if x>=0 and x<h0 and y>=0 and y<v0:
                        count+=(field[y][x]=='w')
                if count==0:
                    return False
    return True

