
def find_missing(lst):
  if not lst: return False
  lens = []
  for list in lst:
    if not list: return False
    
    lens.append(len(list))
  
  lens.sort()
  
  for i in range(len(lens)-1):
    if lens[i] + 1 != lens[i+1]:
      return lens[i] + 1
    
  return False

