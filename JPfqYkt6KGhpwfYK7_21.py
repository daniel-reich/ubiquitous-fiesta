
def replace_the(txt):
  l = []
  txt = txt.split()
  for i in range(len(txt)):
    if txt[i] == "the" and txt[i + 1][0] in "aeiou":
      l.append("an")
    elif txt[i] == "the" and txt[i + 1][0] not in "aeiou":
      l.append("a")
    else:
      l.append(txt[i])
​
  return " ".join(l)

