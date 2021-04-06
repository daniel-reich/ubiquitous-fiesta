
def stmid(string):
  return ''.join([i[0] if len(i) % 2 == 0 else i[len(i) // 2] for i in string.split()])

