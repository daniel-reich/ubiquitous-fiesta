
def is_ascending(s):
  for i in range(1,len(s)//2+1):
    tmp,res = int(s[:i]),''
    while len(res) < len(s):
      res += str(tmp)
      tmp += 1
    if res == s:
      return True
  return False

