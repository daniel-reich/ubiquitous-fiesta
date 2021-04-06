
def special_reverse(s, c):
  l = s.split()
  for i in range(len(l)):
    if l[i][0] == c:
      l[i] = l[i][::-1]
  s = " ".join(l)
  return s

