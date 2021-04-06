
def is_repeated(s):
  l = len(s)
  for i in range(1,l//2+1):
    if s[:i] == s[i:2*i]:
      l = i
      break
  else:
    return False
  return len(s) / l

