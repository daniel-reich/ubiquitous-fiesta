
def stmid(string):
  return ''.join([a[0] if len(a)%2==0  else a[(len(a)//2)] for a in string.split()])

