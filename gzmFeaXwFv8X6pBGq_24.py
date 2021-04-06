
def series_resistance(lst):
  sum =0
  for i in range(len(lst)):
    sum += lst[i]
  if sum<=1:
    str1 = str(sum)+" "+"ohm"
  else:
    str1 = str(sum)+" "+"ohms"
  return str1

