
def can_capture(queens):
  def to_ints(q):
    return ["ABCDEFGH".index(q[0])+1 , int(q[1])]
  q1, q2 = [to_ints(i) for i in queens]
  
  return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])

