
def division(a,b):
  d, s, w = '', str(a//b)+'.', 4
  while a%b:
    a = a%b*10
    d += str(a//b)
    if d[-w:] in d[:-w]: break
  if not d: d='0'
  if a%b==0: return s+d
  i = d.find(d[-w:])
  r = d[i:-w]
  j = (r+r).find(r, 1,-1) 
  if j!=-1: r = r[:j]
  return s+d[:i]+'('+r+')'

