
def domino_chain(dominos):
  arr = list(dominos)
  indd = None
  for ind, d in enumerate(dominos):
    if d not in ('/', ' '):
      arr[ind] = '/'
    else:
      break
  return "".join(arr)

