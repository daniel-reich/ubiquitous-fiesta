
def odd_sort(lst):
  odds = []
  for i in lst:
    if i%2 != 0:
      odds.append(i)
  odds.sort()
  counter = 0
  for i in range(len(lst)):
    if lst[i]%2 != 0:
      lst[i] = odds[counter]
      counter +=1
  return lst

