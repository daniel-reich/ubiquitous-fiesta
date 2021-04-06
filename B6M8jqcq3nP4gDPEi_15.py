
def iso_group(lst):
  if len(lst)==1:
    return lst[0]
  elif all(lst[i]==lst[i+1] for i in range(len(lst)-1)):
    return lst
  if lst[0]==lst[1]:
    x=lst.pop(1)
    lst.append(x)
  else:
    lst.remove(min(lst[0],lst[1]))
  return iso_group(lst)

