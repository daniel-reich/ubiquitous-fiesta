
def helper(lst,el):
  result = {0:0}
  for item in lst:
    if type(item) == list:
      counts = helper(item, el)
      for key,val in counts.items():
        result[key+1] = result.get(key+1, 0) + val
    else:
      if item == el:
        result[0] = result.get(0,0) + 1
  return result
​
def freq_count(lst, el):
  counts = helper(lst, el)
  result = []
  for key in sorted(counts.keys()):
    result.append([key,counts[key]])
    
  return result

