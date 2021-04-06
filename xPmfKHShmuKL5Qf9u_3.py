
def scale_tip(l):
  x=l.index('I')
  i=sum(l[:x])
  r=sum(l[x+1:])
  return'right'if r>i else'left'if i>r else'balanced'

