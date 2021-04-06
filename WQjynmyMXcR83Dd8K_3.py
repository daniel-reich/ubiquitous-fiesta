
def number_of_swaps(lst):
  r=0
  while lst!=sorted(lst):
    for i in range(len(lst)-1):
      if lst[i]>lst[i+1]:
        lst[i],lst[i+1]=lst[i+1],lst[i]
        r+=1
  return r

