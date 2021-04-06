
def even_odd_transform(lst, n):
  for i in range(len(lst)):
    for j in range(n):
      if lst[i] %2==0 :
        lst[i]-= 2
      else :
        lst[i]+= 2
  return lst

