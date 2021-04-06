
def shift_letters(txt, n):
  l = list(txt)
  s = []
  for i in range(len(l)):
    if l[i] == " ":
      s.append(i)
  p = ""
  for i in txt:
    if i != " ":
      p += i
  k = list(p)
  for i in range(n):
    k.insert(0,k.pop())
  for i in s:
    k.insert(i, " ")
  return "".join(k)

