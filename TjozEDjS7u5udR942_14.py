
def sort_authors(lst):
  d = {}
  for x in lst:
    temp = x.split()
    d[temp[len(temp)-1].capitalize()] = lst.index(x)
  
  arr = []
  for k, v in sorted (d.items()) :  
    arr.append(lst[v])
  return arr

