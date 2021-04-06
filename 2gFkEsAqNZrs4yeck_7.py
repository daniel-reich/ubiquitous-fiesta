
def mini_peaks(lst):
  return [lst[i] for i in range(1,len(lst)-1) if lst[i-1] < lst[i] > lst[i+1] ]

