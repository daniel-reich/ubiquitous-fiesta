
def mini_peaks(lst):
  l=[]
  for i in range(1, len(lst)-1):
    if lst[i]>lst[i-1] and lst[i]>lst[i+1]:
      l.append(lst[i])
  return l

