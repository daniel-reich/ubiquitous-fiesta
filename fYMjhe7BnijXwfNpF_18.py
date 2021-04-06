
def stmid(string):
  lst = string.split(" ")
  ans = ""
  for e in lst:
    if len(e) % 2 == 0:
      ans += e[0]
    else:
      ans += e[int(len(e)/2)]
  return ans

