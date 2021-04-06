
def mini_peaks(lst):
  newlist = []
  for x in range(1, len(lst)-1):
    if lst[x] > lst[x-1] and lst[x] > lst[x+1]:
      newlist.append(lst[x])
  return newlist

