
def mini_peaks(lst):
  a = []
  for idx, elem in enumerate(lst):
    if idx != len(lst) - 1 and idx != 0:
      if elem > lst[idx-1] and elem > lst[idx+1]:
        a.append(elem)
  return a

