
def cumulative_sum(lst):
  if len(lst) == 0:
    return lst
  lst2 = [lst[0]]
  counter = 0
  for i in range (len(lst)-1):
    lst2.append(lst2[counter]+lst[i+1])
    counter+=1
  return lst2

