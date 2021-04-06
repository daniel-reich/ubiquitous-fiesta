
def recaman_index(n):
  lst = [0]
  ind=0
  while n not in lst:
    newNum = lst[-1]-len(lst)
    if newNum > 0 and newNum not in lst:
      lst.append(newNum)
    else:
      lst.append(lst[-1]+len(lst))
    ind+=1
  return ind

