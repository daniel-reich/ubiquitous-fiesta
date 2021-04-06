
def difference_two(lst):
  ret = []
  for i in range(len(lst)):
    for j in range(i+1,len(lst)):
      if abs(lst[i]-lst[j])==2:
        ret.append(sorted([lst[i],lst[j]]))
  return sorted(ret,key = lambda x:x[0])

