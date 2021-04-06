
def almost_palindrome(txt):
  i = 0
  k = 0
  copy = ""
  while i < len(txt):
    if txt[i] != txt[-i-1]:
      k += 1
    i += 1
  
  if k < 3 and k != 0:
    return True
  else:
    return False

