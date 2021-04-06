
def tower_of_hanoi(d,m):
  def tow(d, m, st, end):
    if d == 0:
      return [[]]*3
    if m >= 2**(d - 1):
      return [[d]*(end == i) + tow(d-1,m-2**(d - 1),(-st-end)%3,end)[i] for i in [0,1,2]]
    else:
      return [[d]*(st == i) + tow(d-1,m,st,(-st-end)%3)[i] for i in [0,1,2]]
  return tuple(tow(d,m,0,2))

