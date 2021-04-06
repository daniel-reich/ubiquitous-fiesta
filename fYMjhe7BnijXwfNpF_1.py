
def stmid(string):
  return ''.join(i[len(i)//2] if len(i)%2 else i[0] for i in string.split())

