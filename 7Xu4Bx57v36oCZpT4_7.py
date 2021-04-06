
def where_is_waldo(lst):
  a = [x for sublist in lst for x in sublist]
  count = 0
  i = 0
  while i<len(a):
    if a[i]!=a[i+1]: break
    i+=1
  return [int((i+1)/len(lst[0]))+1, (i+1)%len(lst[0])+1 ]

