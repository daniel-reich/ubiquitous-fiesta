
def odd_sort(lst):
  odds = [i for i in lst if i%2==1]
  odds.sort()
  for i in range (len(lst)):
    if lst[i]%2==1:
      lst[i] = odds[0]
      odds.pop(0)
  return lst

