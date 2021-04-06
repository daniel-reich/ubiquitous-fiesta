
def domino_chain(dominos):
  ret = list(dominos)
  for i in range(len(ret)):
    if ret[i]!='|': break
    else: ret[i]='/'
  return ''.join(ret)

