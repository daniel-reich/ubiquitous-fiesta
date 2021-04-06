
def mini_peaks(lst):
  print(lst)
  return [lst[x] for x in range(1,len(lst) - 1) if lst[x] > lst[x-1] and lst[x] > lst[x+1]]

