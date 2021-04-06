
def stmid(string):
  return ''.join(x[len(x)//2] if len(x) % 2 else x[0] for x in string.split())

