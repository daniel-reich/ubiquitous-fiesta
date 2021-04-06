
def color_pattern_times(cols):
  blank = [2]
  for i in range(1,len(cols)):
    if cols[i] == cols[i-1]:
      blank.append(2)
    else:
      blank.append(3)
  return sum(blank)

