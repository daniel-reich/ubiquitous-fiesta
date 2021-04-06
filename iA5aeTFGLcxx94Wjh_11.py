
def delete_occurrences(lst, num):
  
  nl = []
  
​
  for item in lst:
    if item in nl:
      c = nl.count(item)
      if c >= num:
        continue
      else:
        nl.append(item)
    else:
      nl.append(item)
  
  return nl

