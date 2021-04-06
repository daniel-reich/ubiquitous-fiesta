
def color_pattern_times(cols):
  if cols == []:
    return 0
  sum = 2
  for i in range(1, len(cols)):
    if cols[i] != cols[i-1]:
      sum += 1
    sum += 2
  return sum

