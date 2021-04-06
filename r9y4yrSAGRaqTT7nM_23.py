
def find_missing(lst):
  lengths = []
  if lst == []:
    return False
  elif lst == None:
    return False
    
  for small_list in lst:
    if small_list == []:
      return False
    length= len(small_list)
    lengths.append(length)
    
  mini = min(lengths)
  maxi = max(lengths)
  compare = set(range(mini,maxi+1))
  lengths_set = set(lengths)
  difference = compare - lengths_set
  diff = list(difference)
  return diff[0]

