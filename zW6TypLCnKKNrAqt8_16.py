
def left_side(lst):
  def lef(l,n):
    return sum(1 for c in l[0:l.index(n)] if c<n)
  return [lef(lst,c) for c in lst]
​
def right_side(lst):
  def rig(l,n):
    return sum(1 for c in l[l.index(n):] if c<n)
  return [rig(lst,c) for c in lst]

