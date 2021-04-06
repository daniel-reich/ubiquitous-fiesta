
def stmid(string):
  lst = string.split()
  return ''.join([i[0] if not len(i) % 2 else i[int((len(i) - 1) / 2)] for i in lst])

