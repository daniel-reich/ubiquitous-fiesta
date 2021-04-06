
def color_pattern_times(cols):
  if cols==[]:
    return 0
  t=-1
  c=0
  for x in cols:
    if x==c:
      t+=2
    else:
      c=x
      t+=3
  return t

