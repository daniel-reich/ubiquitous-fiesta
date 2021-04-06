
def median(lst):
  x = len(lst)
  lst = sorted(lst)
  if x % 2 != 0:
    return lst[int(x/2-0.5)]
  else:
    return ((lst[int(x/2)] + lst[int((x/2)-1)])/2)

