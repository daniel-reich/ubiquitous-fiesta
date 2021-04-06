
def order(lst):
  ordered = [i for i in range(len(lst))]
  
  for i in range(len(lst)):
    
    for j in range(len(lst) - i - 1):
      if lst[j] > lst[j + 1]:
    
        lst[j], lst[j+1] = lst[j+1],lst[j]
        ordered[j], ordered[j+1] = ordered[j+1], ordered[j]
  
  return ordered

