
def common_elements(lst1, lst2):
  common = []
  short, long = sorted([lst1, lst2], key=len)
  
  for i in long:
    if i in short and i not in common:
      common.append(i)
  
  return common

