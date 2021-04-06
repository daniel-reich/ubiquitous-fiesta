
def simon_says(lst1, lst2):
  x=len(lst1)
  del lst1[x-1]
  del lst2[0]
  equal=True
  for i in range(x-1):
    if lst1[i]!=lst2[i]:
      equal=False
  return equal

