
def complete_binary(s):
  st = str(s)
  while len(st)%8 > 0:
    st = '0'+st
  return st

