
def valid_rondo(s):
  if(len(s)%2==0 or s=='A'):
    return False
  for i in range(0,len(s),2):
    if(s[i]!='A'):
      return False
  if(s[-1]!='A'):
    return False
  return True

