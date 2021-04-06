
def group(lst, size):
​
  to_split = round(len(lst) / size)
  groups = []
​
  for n in range(0, to_split):
​
    group = []
    
    for num in range(n, len(lst), to_split):
      group.append(lst[num])
​
    groups.append(group)
  
  return groups

