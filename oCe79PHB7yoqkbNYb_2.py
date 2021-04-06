
def break_point(num):
  s=list(map(int,str(num)))
  return any(sum(s[:i])==sum(s[i:]) for i in range(len(s)))

