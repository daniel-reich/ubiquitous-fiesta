
def domino_chain(dominos):
  res = list(dominos)
  for ind,i in enumerate(res):
    if i!='|':
      break
    res[ind] = '/'
  return ''.join(res)

