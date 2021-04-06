
def track_robot(*args):
    result=[0,0]
    n=len(args)
    signs=iter((1,1,-1,-1)*n)
    direction=iter(("D", "P")*n)
    for i in args:
        if next(direction)=="P":
            result[0]+=(i*next(signs))
        else:
            result[1]+=(i*next(signs))
    return result

