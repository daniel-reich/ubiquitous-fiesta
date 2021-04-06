
def count_ones(lst):
  count = 0
  if lst[0] == 1 and lst[1] == 1:
    count += 1
  for i in range(1,len(lst)-1):
    if lst[i]==1:
      if lst[i-1] != 1 and lst[i+1] == 1:
        count += 1
  return count

