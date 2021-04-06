
def sum_of_evens(lst):
  sum = 0
  for i in range (len(lst)):
    for j in range (len(lst[i])):
      if (lst[i][j]%2==0):
        sum += lst[i][j]
  return sum

