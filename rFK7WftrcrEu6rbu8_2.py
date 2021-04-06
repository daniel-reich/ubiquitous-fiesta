
class Node:
  def __init__(self,d):
    self.d=d
    self.l=self.r=None
class BST:
  def __init__(self):self.h=None
  def insert(self,d):
    n=Node(d)
    if self.h==None:self.h=n
    else:
      c=self.h
      while 1:
        if d>c.d and c.r:c=c.r
        elif d<c.d and c.l:c=c.l
        elif d>c.d:c.r=n;break
        else:c.l=n;break
    return self.h
  def traverse(self):
    r,v=[],[]
    o=self.h
    if o:v.append(o);r.append(o.d)
    c=o
    while c:
        if c.l:r.append(c.l.d);v.append(c.l)
        if c.r:r.append(c.r.d);v.append(c.r)
        v.pop(0)
        if not v:break
        c=v[0]
    return r

