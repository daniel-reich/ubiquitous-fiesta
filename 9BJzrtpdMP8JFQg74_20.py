
def twins(lst):
  for x in range(len(lst)):   
    if sum(lst[:x])==sum(lst[x:]):
      return x

