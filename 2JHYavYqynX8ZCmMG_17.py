
def ascii_sort(lst):
  sums=[]
  for i in range(0,len(lst)):
    total=0
    for k in range(0,len(lst[i])):
      total+=ord(lst[i][k])
    sums.append(total)
  if sums[0] < sums[1]:
    small=lst[0]
  else:
    small=lst[i]
  return small

