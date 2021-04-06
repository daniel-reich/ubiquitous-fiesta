
def centroid(*args):
    x1,y1,x2,y2,x3,y3=args
    if (x2-x1) == 0 and (x3-x2) == 0:
        return False
    elif (x2-x1)==0:
        if (y3-y2)/(x3-x2) != (y3-y1)/(x3-x1):
            x,y = (x1+x2+x3)/3.0, (y1+y2+y3)/3.0
            x=round(x, 2)
            y=round(y,2)
            return (x,y)
        else:
            return False
    elif (x3-x2)==0:
        if (y2-y1)/(x2-x1) != (y3-y1)/(x3-x1):
            x,y = (x1+x2+x3)/3.0, (y1+y2+y3)/3.0
            x=round(x, 2)
            y=round(y,2)
            return (x,y)
        else:
            return False
    elif (x3-x1)==0:
        if (y2-y1)/(x2-x1) != (y3-y2)/(x2-x1):
            x,y = (x1+x2+x3)/3.0, (y1+y2+y3)/3.0
            x=round(x, 2)
            y=round(y,2)
            return (x,y)
        else:
            return False
​
    else:
        if (y2-y1)/(x2-x1) != (y3-y2)/(x3-x2):
            x,y = (x1+x2+x3)/3.0, (y1+y2+y3)/3.0
            x=round(x, 2)
            y=round(y,2)
            return (x,y)
        else:
            return False

