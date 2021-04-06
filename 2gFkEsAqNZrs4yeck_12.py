
def mini_peaks(lst):
  res = []
  for i in range(1,len(lst)-1):
    if lst[i] > lst[i-1] and lst[i] > lst[i+1]:
      res.append(lst[i])
  return res

