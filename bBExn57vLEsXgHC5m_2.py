
def same_line(lst):
  x1,y1=lst[0]
  x2,y2=lst[1]
  x3,y3=lst[2]
  if x1==x2 and x2==x3: return True
  if x2-x1==0 or x3-x2==0: return False
  return ((y2-y1)/(x2-x1))==((y3-y2)/(x3-x2))

