
def odd_sort(lst):
  oddlst = [i for i in sorted(lst) if i%2!=0]
  evenidx =[j for j in range(len(lst)) if lst[j]%2==0]
  for x in evenidx:
    oddlst.insert(x, lst[x])
  return oddlst

