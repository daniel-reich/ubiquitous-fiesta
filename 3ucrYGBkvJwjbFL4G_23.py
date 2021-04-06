
def reversible_inclusive_list(start, end):
  if start< end:
    return [i for i in range(start ,end+1)]
  else:
    return [i for i in range(start ,end-1,-1)]

