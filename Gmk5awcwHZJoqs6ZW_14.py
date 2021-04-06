
def largest_island(lst):
    def find_starter(lst,checked):
            for y in range(ylen):
                for x in range(xlen):
                    if lst[y][x]==1 and (y,x) not in checked:
                        return (y,x)
            return False
        
    checked,ylen,xlen,to_check=[],len(lst),len(lst[0]),[]
    neigh=[(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(1,1),(-1,1),(1,-1)]
    res=[]
    while find_starter(lst,checked):
        count=0
        to_check=[find_starter(lst,checked,)]
        while to_check:            
            for cell in to_check:
                to_check.remove(cell)
                y,x=cell[0],cell[1]
                count+=1
                checked.append((y,x))
                for n in neigh:
                    if y+n[0] in range(ylen) and x+n[1] in range(xlen) and lst[y+n[0]][x+n[1]] ==1 and (y+n[0],x+n[1]) not in checked:
                        if (y+n[0],x+n[1]) not in to_check:
                            to_check.append((y+n[0],x+n[1])) 
        res.append(count)    
    return max(res)

