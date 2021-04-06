
def next_letters(s):
  i = len(s)-1
  return checkNext(s,i)
  
def checkNext(s,i):
  a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  if s=='':
    return 'A'
  elif s[i]!='Z':
    return s[:i]+a[a.index(s[i])+1]
  else:
    return checkNext(s[:i],i-1)+'A'

