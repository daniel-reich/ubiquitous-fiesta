
def complete_binary(s):
  e=len(s)%8
  if e==0:
    return s
  return '0'*(8-e)+s

