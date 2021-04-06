
import operator
def on_rectangle_bounds(points):
    Liste=points
    if int(len(points))<=2:
        return True
    else:
        Xmin=sorted(Liste,key=operator.itemgetter(0))[0][0]
        Xmax=sorted(Liste,key=operator.itemgetter(0))[int(len(sorted(Liste,key=operator.itemgetter(0))))-1][0]
        Ymin=sorted(Liste,key=operator.itemgetter(1))[0][1]
        Ymax=sorted(Liste,key=operator.itemgetter(1))[int(len(sorted(Liste,key=operator.itemgetter(0))))-1][1]
        for p in points:
            if p[0]!=Xmin:
                if p[0]!=Xmax:
                    if p[1]!=Ymin:
                        if p[1]!=Ymax:
                            return False
        return True

