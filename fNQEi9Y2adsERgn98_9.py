
def dist(p,q):
    return ((p[0]-q[0])**2+(p[1]-q[1])**2)**0.5
def perimeter(lst):
    l1 = dist(lst[0],lst[1])
    l2 = dist(lst[1],lst[2])
    l3 = dist(lst[0],lst[2])
    return  round(l1+l2+l3,2)

