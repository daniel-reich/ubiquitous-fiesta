
def even_odd_transform(lst, n):
  for k in range(0,n):
    for i in range(0, len(lst)):
        if lst[i] % 2 == 0:
          lst[i]-=2
        else:
          lst[i]+=2
  return lst

