
def complete_binary(s):
  n = len(str(s))%8
  if n==0:
    return s
  else:
    nd = 8-n
  return str("0"*nd)+str(s)

