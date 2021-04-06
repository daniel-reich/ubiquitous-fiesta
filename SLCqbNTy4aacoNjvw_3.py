
def remove_dups(lst):
  result = []
  
  for i in lst:
    if i not in result:
      result.append(i)
​
  return result

