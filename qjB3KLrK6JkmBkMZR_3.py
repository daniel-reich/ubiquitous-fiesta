
def can_capture(queens):
  q1,q2 = map(list,queens)
  x1,y1 = list(q1)
  x2,y2 = list(q2)
  return abs(int(y1)-int(y2)) == abs(ord(x1)-ord(x2)) or \
    y1 == y2 or x1 == x2

