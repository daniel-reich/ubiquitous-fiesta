
def odd_sort(lst):
  temp = []
  for i in range(len(lst)):
    if lst[i] % 2 == 1:
      temp.append(lst[i])
      lst[i] = '#'
  temp = sorted(temp)
  for i in range(len(lst)-1,-1,-1):
    if lst[i] == '#':
      lst[i] = temp.pop()
  return lst

