
def overlapping_rectangles(rect1, rect2):
  x1,y1,w1,l1=rect1
  x2,y2,w2,l2=rect2
  A=[]
  for i in range(x1, x1+w1):
    for j in range(y1, y1+l1):
      A.append((i,j))
  B=[]
  for i in range(x2, x2+w2):
    for j in range(y2, y2+l2):
      B.append((i,j))
  return len(set(A)&set(B))

