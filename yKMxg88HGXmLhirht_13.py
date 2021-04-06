
def add_letters(a):
  alpha = "abcdefghijklmnopqrstuvwxyz"
  d, s = dict(), 0
  for c in alpha: d[c] = alpha.index(c)+1
  for c in a: s += d[c]
  return alpha[s%26-1]

