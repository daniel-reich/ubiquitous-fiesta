
def stmid(s):
  return ''.join([i[0] if not len(i)%2 else i[len(i)//2] for i in s.split()])

