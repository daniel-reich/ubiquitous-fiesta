
def unique_lst(lst):
  filt = []
  for i in lst:
    if i > 0 and i not in filt:
      filt.append(i)
  return filt

