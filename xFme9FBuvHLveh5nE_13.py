
def is_zygodrome(num):
  s = str(num)
  if len(s) < 2 or s[0] != s[1] or s[-1] != s[-2]:
    return False
  for x in range(1, len(s)-2):
    if s[x] != s[x-1] and s[x] != s[x+1]:
      return False
  return True

