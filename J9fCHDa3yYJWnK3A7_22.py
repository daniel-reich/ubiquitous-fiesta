
def is_happy(n):
  n = str(n)
  rep = []
  while int(n) != 1:
      ans = 0
      for i in n: ans += int(i)*int(i)
      n = str(ans)
      if ans not in rep: rep.append(ans)
      else: break
  if int(n) == 1: return True
  return False

