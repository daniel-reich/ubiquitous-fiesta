
def complete_binary(s):
  if len(s)%8==0:
    return s
  n = 1
  while (n+len(s))%8 != 0:
    n = n + 1
  return n*'0' + s

