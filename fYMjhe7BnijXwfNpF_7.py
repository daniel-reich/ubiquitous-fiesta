
def stmid(string):
  return ''.join([x[0] if len(x) % 2 == 0 else x[len(x)//2] for x in string.split()])

