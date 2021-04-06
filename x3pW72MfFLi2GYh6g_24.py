
def is_scalable(lst):
  count = 0
  for i in range(len(lst)-1):
    if lst[i+1]- lst[i]<=5:
      count +=1
  return (count == len(lst)-1)

