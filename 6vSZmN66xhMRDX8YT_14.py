
def advanced_sort(lst):
  unique = [] 
  for x in lst:
    if x not in unique:
      unique.append(x)
      
  result = []
  for uni_obj in unique:
    temp = []
    while uni_obj in lst:
      lst.remove(uni_obj)
      temp.append(uni_obj)
    result.append(temp)
  return result

