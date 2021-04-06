
def area(p1,p2,p3):
    return abs((p1[0]*(p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1]))/2)
​
​
def within_triangle(p1, p2, p3, test):
    return area(p1,p2,test) + area(p1,p3,test) + area(p2,p3,test) == area(p1,p2,p3)

