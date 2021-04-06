
def sum_of_evens(lst):
  sum = 0
  for i, row in enumerate(lst):
    for j, col in enumerate(lst[i]):
      if lst[i][j]%2 == 0:
        sum = sum + lst[i][j]
        
  return sum

