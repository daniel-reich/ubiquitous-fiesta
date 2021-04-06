
def partitions(n):
  if n == 0:
    return 1
  if n <= 3:
    return n
    
  parts = all_parts([1] * n)
  parts = organize_parts(parts, 0)  
​
  return len(parts)
  
  
  
def organize_parts(parts, i):
  if len(parts) <= 1:
    return parts
  ret = []
  for part in parts:
    if len(part)>1 and isinstance(part[1], list):
      for p in organize_parts(part[1:], i + 1):
        newpart = sorted([part[0]] + p)
        if newpart not in ret:
          ret.append(newpart)
    elif sorted(part) not in ret:
      ret.append(sorted(part))
  return ret
    
  
def all_parts(parts):
  if len(parts) <= 1:
    return parts
  return [[i+1] + all_parts(parts[i+1:]) for i in range(len(parts))]

