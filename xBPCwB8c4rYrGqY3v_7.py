
def missing(lst):
  x = 0
  if lst[1] - lst[0] == lst[2] - lst[1] or lst[1] - lst[0] < lst[2] - lst[1]:
    x = lst[1] - lst[0]
  else:
    x = lst[2] - lst[1]
  lst2 = []
  x = int(x*100)
  for i in range(int(lst[0]*100), int((lst[-1]+1)*100), x):
    lst2.append(i/100)
  for i in lst2:
    if i not in lst:
      return i

