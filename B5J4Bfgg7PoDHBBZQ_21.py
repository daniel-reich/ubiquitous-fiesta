
def within_triangle(p1, p2, p3, test):
  area = abs((p1[0]*(p2[1] - p3[1]) + p2[0]*(p3[1] - p1[1]) + p3[0]*(p1[1]-p2[1]))/2)
  a1 = abs((test[0]*(p2[1] - p3[1]) + p2[0]*(p3[1] - test[1]) + p3[0]*(test[1]-p2[1]))/2)
  a2 = abs((p1[0]*(test[1] - p3[1]) + test[0]*(p3[1] - p1[1]) + p3[0]*(p1[1]-test[1]))/2)
  a3 = abs((p1[0]*(p2[1] - test[1]) + p2[0]*(test[1] - p1[1]) + test[0]*(p1[1]-p2[1]))/2)
  return a1 + a2 + a3 == area

