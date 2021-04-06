
def within_triangle(p1, p2, p3, test):
    a=0.5*(p1[0]*(p2[1]-p3[1])+p2[0]*(p3[1]-p1[1])+p3[0]*(p1[1]-p2[1]))
    a1=0.5*(p1[0]*(p2[1]-test[1])+p2[0]*(test[1]-p1[1])+test[0]*(p1[1]-p2[1]))
    a2=0.5*(test[0]*(p2[1]-p3[1])+p2[0]*(p3[1]-test[1])+p3[0]*(test[1]-p2[1]))
    a3=0.5*(p1[0]*(test[1]-p3[1])+test[0]*(p3[1]-p1[1])+p3[0]*(p1[1]-test[1]))
    return abs(a)==abs(a1)+abs(a2)+abs(a3)

