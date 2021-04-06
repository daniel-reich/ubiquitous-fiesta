
def ping_pong(lst, win):
  s=['Pong!' if i%2!=0 else lst[i//2] for i in range(2*len(lst))]
  if win:
    return s
  return s[:-1]

