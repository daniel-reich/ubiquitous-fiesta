
def is_alpha(word):
  alpha = "abcdefghijklmnopqrstuvwxyz"
  s = 0
  for c in word:
    if c.lower() in alpha:
      s += alpha.index(c.lower())+1
  
  return s % 2 == 0

