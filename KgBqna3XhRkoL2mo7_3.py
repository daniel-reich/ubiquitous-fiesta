
def decrypt(s):
  i,res = len(s)-1,''
  while i >= 0:
    if s[i] == '#':
      res = chr(int(s[i-2:i])+96) + res
      i -= 3
    else:
      res = chr(int(s[i])+96) + res
      i -= 1
  return res

