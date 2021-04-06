
def twins(lst):
  for a in range(1,len(lst)):
    if sum(lst[:a]) == sum(lst[a:]): return a

