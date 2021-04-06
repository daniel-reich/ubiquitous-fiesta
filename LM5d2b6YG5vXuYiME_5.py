
def can_enter_cave(lst):
    for i in range(len(lst)):
        if lst[i][0]==0:
            to_check=[(i,0)]
            break
    checked=[]
    neighbours=[(0,1),(0,-1),(1,0),(-1,0)]
    while to_check:
        for cell in to_check:
            y,x=cell[0],cell[1]
            to_check.remove((y,x))
            checked.append((y,x))
            for neigh in neighbours:
                y,x=cell[0]+neigh[0],cell[1]+neigh[1]
                if y in range(len(lst)) and  x in range(len(lst[0])) and lst[y][x]==0 and (y,x) not in checked:                    
                    if  x==len(lst[0])-1:
                        return True
                    to_check.append((y,x))
    return False

