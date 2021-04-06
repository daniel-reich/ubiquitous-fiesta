
def relation_lst(lst):
  arr = []
  for i in range(len(lst)):
    for j in range(i,len(lst),1):
      #print(i,j)
      a = tuple(sorted([lst[i],lst[j]]))
      arr.append(a)
  return sorted(arr)

