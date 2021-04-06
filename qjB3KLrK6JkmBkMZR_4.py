
def can_capture(q):
  return (abs(ord(q[0][0])-ord(q[1][0])) == abs(int(q[0][1])-int(q[1][1])) or
    q[0][0] == q[1][0] or q[0][1] == q[1][1])

