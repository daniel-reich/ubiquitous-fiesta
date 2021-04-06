
def missing(lst):
  dist = (lst[-1] - lst[0]) / len(lst)
  
  print(dist)
  
  for i in range(len(lst) - 1):
    if lst[i+1] != (lst[i] + dist):
      return lst[i] + dist

