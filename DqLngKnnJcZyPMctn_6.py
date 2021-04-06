
def stock_picker(lst):
  maxdiff = 0
  for i in range(len(lst)-1):
    for j in range(len(lst)-1-i-1):
      if lst[i+j+1] > lst[i]:
        if lst[i+j+1] - lst[i] > maxdiff:
          maxdiff = lst[i+j+1] - lst[i]
  if maxdiff == 0:
    return -1
  else:
    return maxdiff

