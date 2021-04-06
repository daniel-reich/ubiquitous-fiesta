
def stmid(string):
  words = string.split()
  o = [word[0] if len(word) % 2 == 0 else word[len(word) // 2] for word in words]
  return ''.join(o)

