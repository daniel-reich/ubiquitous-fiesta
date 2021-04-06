
def color_pattern_times(cols):
  print(cols)
  t=len(cols)
  c=0
  for i in range(1,len(cols)):
    if cols[i] != cols[i-1]:
      c +=1
  return t*2+c

