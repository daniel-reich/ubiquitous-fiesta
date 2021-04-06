
def odd_sort(lst):
  odds,i = sorted([x for x in lst if x%2]),0
  for j in range(len(lst)):
    if lst[j]%2:
      lst[j] = odds[i]
      i+=1
  return lst

