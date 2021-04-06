
def bomb(lst):
    for x in range(51):
        for y in range(51):
            if (x-lst[0][0])**2+(y-lst[0][1])**2 ==round((lst[0][2]*.343)**2) and \
            (x-lst[1][0])**2+(y-lst[1][1])**2==round((lst[1][2]*.343)**2)  and \
            (x-lst[2][0])**2+(y-lst[2][1])**2 ==round((lst[2][2]*.343)**2):          
                return x,y

