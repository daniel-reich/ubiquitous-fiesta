
def valid_rondo(s):
  if len(s) == 1 : return False
  st = 'A'+ ''.join(chr(x) +'A' for x in range(66, ord(s[-2])+1))
  return s ==st

