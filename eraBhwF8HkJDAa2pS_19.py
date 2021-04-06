
def pirates_killed(gold, tolerance):
  lst=[]
  lst2=[]
  for i in gold:
    lst.append(max(gold)-i)
  for i in range(len(tolerance)):
    if tolerance[i]<lst[i]:
      return True
  return False

