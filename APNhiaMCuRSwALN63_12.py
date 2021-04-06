
def almost_palindrome(txt):
  count=0
  t = txt[::-1]
  if txt==t:
    return False
  else:
    for z,s in zip(t,txt):
      if z!=s:
        count+=1
      if count>2:
        return False
  return True

