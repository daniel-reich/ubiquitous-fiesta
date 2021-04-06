
# (a,b,c) -- dimensions of the brick
# (w,h) -- dimensions of the hole
def does_brick_fit(a,b,c, w,h):
    lst=[a,b,c]
    lst.sort()
    if lst[0]<=w and lst[1]<=h:
        return True
    elif lst[0]<=h and lst[1]<=w:
        return True 
    else:
        return False

