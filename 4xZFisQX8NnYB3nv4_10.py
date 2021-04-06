
def maximum_seating(lst):
  count = 0
  for i in range(len(lst)):
    if lst[i]==0:
      left = lst[max(0,i-2):i].count(1)
      right = lst[i+1:min(len(lst),i+3)].count(1)
      if left==0 and right==0:
        lst[i] = 1
        count+=1
  return count

