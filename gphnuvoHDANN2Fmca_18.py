
def odd_sort(lst):
  odd = []
  for i in range(0,len(lst)):
    if lst[i] % 2 == 1:
      odd.append(lst[i])
      lst[i] = "*"
  
  sorted = []
  min_pos = 0
  while len(odd) != 0:
    min_pos = 0
    for j in range(0,len(odd)):
      if odd[j] < odd[min_pos]:
        min_pos = j
    sorted.append(odd[min_pos])
    odd.pop(min_pos)
    
  for i in range(0,len(lst)):
    if lst[i] == "*":
      lst[i] = sorted[0]
      sorted.pop(0)
  return lst

