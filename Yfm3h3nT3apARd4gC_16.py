
def rolls(lst):
  total = sum(lst)
  lenght = len(lst)
  for i,j in enumerate(lst):
    if j == 1 and (i != (lenght-1)):
      total = total - lst[i+1]
    elif j == 6 and (i != (lenght-1)):
      total = total + lst[i+1]*2 - lst[i+1]
  return total

