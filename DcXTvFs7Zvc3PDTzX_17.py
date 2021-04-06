
def validate_binary(b):
  l = len(b)
  par = int(b[l-1])
  s = 0
  for i in range(l-1):
    s = s + int(b[i])
  if par == s%2:
    return True
  else:
    return False

