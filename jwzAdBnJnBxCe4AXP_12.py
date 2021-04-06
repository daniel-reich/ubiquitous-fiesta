
def rearranged_difference(num):
  num = str(num)
  max = sorted(num)
  min = sorted(num, reverse=True)
  newmax = ""
  newmin = ""
  for num in max:
    newmax += num
  for num in min:
    newmin += num
  newmax = int(newmax)
  newmin = int(newmin)
  ans = newmax - newmin
  
  return -ans

