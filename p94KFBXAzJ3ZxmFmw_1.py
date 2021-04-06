
def ascii_capitalize(txt):
  ans = ''
  for x in txt:
    if ord(x) % 2 == 0:
      ans += x.upper()
    else:
      ans += x.lower()
  return ans

