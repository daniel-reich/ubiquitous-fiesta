
def who_goes_free(n, k):
  lst = []
  kill = 0
  
  for x in range(0,n):
    lst.append(x)
  
  while len(lst) != 1:
    temp = []
    for x in lst:
      kill = kill + 1
      if kill != k:
        temp.append(x)
      else:
        kill = 0
    lst = temp
    
  return lst[0]

