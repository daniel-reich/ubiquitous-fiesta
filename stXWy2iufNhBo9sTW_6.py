
def valid_rondo(s):
  if len(s)<3 or len(s)%2==0:
    return False
  else:
    for x in range(0,len(s),2):
      if s[x]!='A':
        return False
  return True

