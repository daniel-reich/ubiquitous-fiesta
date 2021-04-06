
def color_pattern_times(cols):
  g=0
  for i in range(len(cols)-1):
    if cols[i]!=cols[i+1]:
      g+=1
  return len(cols)*2+g

