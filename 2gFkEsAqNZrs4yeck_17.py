
def mini_peaks(lst):
  lst2 = []
  for i in range(1,len(lst)-1):
    if lst[i] > lst[i-1] and lst[i+1] < lst[i]:
      lst2.append(lst[i])
  return lst2

