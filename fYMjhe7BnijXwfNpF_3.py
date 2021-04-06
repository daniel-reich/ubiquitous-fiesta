
def stmid(string):
  return ''.join(s[0] if len(s)%2==0 else s[len(s)//2] for s in string.split())

