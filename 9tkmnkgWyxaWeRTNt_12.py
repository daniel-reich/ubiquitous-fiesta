
def median(lst):
  lst.sort()
  if len(lst) % 2:
    return lst[int(len(lst) / 2)]
  else:
    return (lst[int(len(lst) / 2)] + lst[int(len(lst) / 2) - 1] ) /2

