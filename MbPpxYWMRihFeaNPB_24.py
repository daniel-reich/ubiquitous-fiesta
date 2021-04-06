
def sum_of_evens(lst):
  k=0
  for i in range(len(lst)):
    for j in range(len(lst[i])):
      if lst[i][j]%2==0:
        k=k+lst[i][j]
  return k

