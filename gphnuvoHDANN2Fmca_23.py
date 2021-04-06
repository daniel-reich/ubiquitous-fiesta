
def odd_sort(lst):
  odds = []
  for i in range(len(lst)):
    if lst[i]%2==1:
      odds.append(lst[i])
      lst[i] = '_'
  odds.sort()
  k = 0
  for i in range(len(lst)):
    if lst[i] == '_':
      lst[i] = odds[k]
      k += 1
  return lst

