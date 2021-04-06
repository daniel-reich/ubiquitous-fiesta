
def sum_of_slices(lst):
  o, j = [], 0
  for i in lst:
    if j+i<=100:
      j += i
    else:
      o.append(j)
      j = i
  o.append(j) #last num
  return o

