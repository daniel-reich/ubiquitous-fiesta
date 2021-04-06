
def odd_sort(lst):
  b=[]
  for i in lst:
    if i%2!=0:
      b.append(i)
  b.sort()
  x=0
  for i in range (len(lst)):
    if lst[i] in b:
      lst[i]=b[x]
      x+=1
  return lst

