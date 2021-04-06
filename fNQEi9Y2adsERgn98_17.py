
def dist(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**.5
​
def perimeter(lst):
    return round(dist(lst[0][0],lst[0][1],lst[1][0],lst[1][1]) + dist(lst[0][0],lst[0][1],lst[2][0],lst[2][1]) + dist(lst[2][0],lst[2][1],lst[1][0],lst[1][1]),2)

