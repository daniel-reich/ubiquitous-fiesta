
def on_rectangle_bounds(Points):
    if len(Points)<=2:
        return True
    
    xsort=sorted(Points)
    xmax=xsort[len(Points)-1][0]
    xmin=xsort[0][0]
    
    ysort=sorted(Points , key=lambda Points : Points[1])
    ymax=ysort[len(Points)-1][1]
    ymin=ysort[0][1]
    
    for i in range(len(Points)):
        if Points[i][0]!=xmax:
            if Points[i][0]!=xmin:
                if Points[i][1]!=ymax:
                    if Points[i][1]!=ymin:
                        return False
    return True

