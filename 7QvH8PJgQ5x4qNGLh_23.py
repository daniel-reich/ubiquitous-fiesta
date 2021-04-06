
def countdown(n, txt):
  res = ""
  for i in range(n,0,-1):
    res += str(i) + ". "
  return res + txt.upper() + "!"

