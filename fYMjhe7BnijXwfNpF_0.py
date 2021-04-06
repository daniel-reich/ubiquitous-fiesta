
def stmid(s):
  return ''.join(w[[0, len(w) // 2][len(w) % 2]] for w in s.split())

