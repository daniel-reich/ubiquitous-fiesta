
def twins(lst):
  half=sum(lst)/2
  for i in range(0,len(lst)):
    if sum(lst[0:i])==half:
      return i
    else:
      pass

