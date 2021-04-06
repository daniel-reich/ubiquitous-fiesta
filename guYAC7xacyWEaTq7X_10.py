
def is_autobiographical(n):
  s=str(n)
  return all(s.count(str(i))==int(s[i]) for i in range(len(s)))

