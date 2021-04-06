
def landscape_type(lst):
  maxp = -1
  minp = -1
  for i in range(1,len(lst)-1):
    if lst[i-1] < lst[i] and lst[i] > lst[i+1]:
      print(lst[i-1],lst[i],lst[i+1])
      if maxp == -1 and lst[i] != lst[0] and lst[i] != lst[-1]:
        maxp = i
      else:
        return 'neither'
  for i in range(1,len(lst)-1):
    if lst[i-1] > lst[i] and lst[i] < lst[i+1]:
      if minp == -1 and lst[i] != lst[0] and lst[i] != lst[-1]:
        minp = i
      else:
        return 'neither'
  if maxp != -1 and minp == -1:
    if maxp != 0 or maxp != len(lst):
      return 'mountain'
    else: 
      return 'neither'
  elif minp != -1 and maxp == -1:
    if minp != 0 or minp != len(lst):
      return 'valley'
    else: 
      return 'neither'
  else:
    return 'neither'

