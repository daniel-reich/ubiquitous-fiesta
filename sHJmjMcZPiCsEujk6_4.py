
def pilish_string(txt):
  pi = str(314159265358979)
  count = 0
  pipos = 0
  ans = ""
  for i in txt:
    ans += i
    count += 1
    if count == int(pi[pipos]):
      ans += " "
      pipos += 1
      count = 0
    if pipos >= len(pi):
      return ans[:-1]
  if count == 0:
    return ans[:-1]
  else:
    return ans + (ans[-1])*(int(pi[pipos])-count)

