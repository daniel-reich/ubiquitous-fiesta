
def ping_pong(lst, win):
  out = []
  if win == True:
    for i in lst:
      out.append(i)
      out.append('Pong!')
    return out
  else:
    for i in range(0,len(lst)):
      out.append(lst[i])
      if i != len(lst)-1:
        out.append('Pong!')
    return out

