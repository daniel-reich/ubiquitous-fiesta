
def can_exit(lst, y=0, x=0, visited=set()):
    if y==len(lst)-1 and x == len(lst[0])-1:
        return True
    adjacents = {(y-1, x), (y+1, x), (y, x-1), (y, x+1)}
    adjacents = {(y_,x_) for y_,x_ in adjacents if 0<=y_<len(lst) and 0<=x_<len(lst[0]) and not lst[y_][x_]}
    return any(can_exit(lst, y_, x_, visited |{(y,x)}) for y_,x_ in adjacents if (y_,x_) not in visited)

