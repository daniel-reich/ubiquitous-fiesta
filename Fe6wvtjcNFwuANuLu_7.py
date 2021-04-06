
def ping_pong(lst, win):
  res = []
  for l in lst:
    res.extend([l,'Pong!'])
  if not win:
    res = res[:-1]
  return res

