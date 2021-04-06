
def get_path_length(world, width, height):
    list2=[]
    list1=world.split(',')
    moves=[(1,0),(0,1),(1,1),(-1,0),(0,-1),(-1,-1),(-1,1),(1,-1)]
    t=[]
    for i in range(0,height*width,width):
        list2.append(list1[i:i+int(width)])
    for i in range(len(list2)):
        for x in range(len(list2[i])):
            if list2[i][x]=='m':
                m=(i,x)
            elif list2[i][x]=='h':
                h=(i,x)
            elif list2[i][x]=='t':
                t.append((i,x))
    res = list(set(tuple(map(lambda i, j: i + j, m, moves[i])) for i in range(len(moves))))
    for count in range(width*height-len(t)+1):
        res2=[]
        res3=[]
        if count==width*height-len(t):
            return (-1)
        res=[i for i in res if i not in t]
        for i in res:
            if i==h:
                return count+1
        for i in res:
            if i[0]<height and i[0]>=0 and i[1]<width and i[1]>=0:
                res3.append(i)
        for x in range(len(res3)):
                for i in range(len(moves)):
                    res2.append(tuple(map(lambda i, j: i + j, res3[x], moves[i])))
        res=list(set(res2))

