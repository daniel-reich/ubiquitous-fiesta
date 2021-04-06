
def swap_two(txt):
  k = len(txt)%4
  st = ''.join(txt[i+2:i+4]+txt[i:i+2] for i in range(0,len(txt)-k,4))
  if k:
    st += txt[-k:]
  return st

