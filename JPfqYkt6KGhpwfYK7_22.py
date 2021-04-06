
def replace_the(t):
  l = t.split()
  out = []
  for i in range(len(l)):
    if l[i]=="the":
      if l[i+1][0] in "aeiou":  out.append("an")
      else: out.append("a")
    else: out.append(l[i])
  return " ".join(x for x in out)

