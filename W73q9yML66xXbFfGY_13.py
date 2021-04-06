
def color(a,b):
  if a==b:
    return a
  else:
    if set([a,b])=={'R', 'G'}:
      return 'B'
    elif set([a,b])=={'R', 'B'}:
      return 'G'
    else:
      return 'R'
def coloured_triangle(row):
  s=row
  while len(s)>1:
    t=''
    for i in range(len(s)-1):
      t+=color(s[i],s[i+1])
    s=t
  return s

