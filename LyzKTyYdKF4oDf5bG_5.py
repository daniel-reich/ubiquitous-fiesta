
def find_longest(s):
  lens = []
  s = list(s.lower())
  for i in s:
    if s.index(i) != (len(s))-1:
        if i == """'""":
          s[s.index(i)+1] = ''
    if i not in "qwertyuiopasdfghjklzxcvbnm ":
      s[s.index(i)] = ''
  s = ''.join(s)
  x = s.split()
  for i in x:
    lens.append(len(i))
  return x[lens.index(max(lens))]

