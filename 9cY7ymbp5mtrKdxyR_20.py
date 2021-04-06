
def encryption(txt):
  txt = txt.replace(" ", "")
  l = len(txt)
  r = int((l** 0.5) // 1)
  if r**2 < l: c = r+1
  else: c = r
  txt2 = ""
  for i in range(c):
    temp = ""
    for j in range(i, len(txt), c):
      temp += txt[j]
    txt2 += temp + " "
  return txt2[:-1]

