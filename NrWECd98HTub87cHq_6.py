
def overlapping_rectangles(rect1, rect2):
    coord1=[]
    coord2=[]
    for x in range(rect1[0],rect1[0]+rect1[2]+1):
        for y in range (rect1[1],rect1[1]+rect1[3]+1):
            coord1=coord1+[[x,y]]
    for x in range(rect2[0],rect2[0]+rect2[2]+1):
        for y in range (rect2[1],rect2[1]+rect2[3]+1):
            coord2=coord2+[[x,y]]
    coordinter=[value for value in coord1 if value in coord2]
    if len(coordinter)==0: return 0
    else:return (max(coordinter)[0]-min(coordinter)[0])*(max(coordinter)[1]-min(coordinter)[1])

