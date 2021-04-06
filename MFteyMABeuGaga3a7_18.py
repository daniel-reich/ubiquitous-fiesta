
def color_pattern_times(cols):
  c = 0
  for i in range(len(cols)-1):
    if cols[i] != cols[i+1]:
      c+=1
      
  return len(cols)*2 + c

