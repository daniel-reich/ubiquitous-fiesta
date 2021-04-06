
def rolls(lst):
  sum = lst[0]
  for i in range(1, len(lst)):
    if lst[i-1] == 6:
      sum += (lst[i]*2)
    elif lst[i-1] != 1:
      sum += lst[i]
  return(sum)

