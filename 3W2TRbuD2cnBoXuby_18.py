
def collect(s, n):
  lst = [s[i:i+n] for i in range(0, len(s), n)]
  if len(lst[-1]) != n:
    lst.pop()
  return sorted(lst)

