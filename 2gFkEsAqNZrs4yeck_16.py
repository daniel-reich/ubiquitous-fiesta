
def mini_peaks(lst):
  return [lst[ii] for ii in range(1,len(lst)-1) if lst[ii-1]<lst[ii]>lst[ii+1]]

