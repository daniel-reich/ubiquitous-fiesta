
def within_triangle(p1, p2, p3, test):
  return area([p1,p2,p3])==area([test,p1,p2])+area([test,p2,p3])+area([test,p1,p3])
    
def area(p_l):
  return abs(sum(p_l[i%3][0]*(p_l[(i+1)%3][1]-p_l[(i+2)%3][1]) for i in range(3)))

