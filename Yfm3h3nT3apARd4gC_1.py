
def rolls(lst):
  total = lst[0]
  for i in range(1,len(lst)):
    if lst[i-1] == 6:
      total += (lst[i] * 2)
    elif lst[i-1] in range(2,6):
      total += lst[i]
  return total

