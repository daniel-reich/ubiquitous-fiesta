
def min_palindrome_steps(txt):
  inv, out=txt[::-1],-1
  if(txt== inv):
    return 0
  for i in range (len(inv),0,-1):
    if (txt+inv[i:]==(txt+inv[i:])[::-1]):
      out = len(inv[i:])
      break
  return out

