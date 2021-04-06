
def even_odd_transform(lst, n):
  for _ in range(n):
    for i in range(len(lst)):
      lst[i] +=  -2 if lst[i]%2==0 else 2
  return lst

