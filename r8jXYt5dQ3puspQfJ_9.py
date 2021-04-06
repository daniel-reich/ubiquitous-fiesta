
def split(txt):
  txt1 = ""
  txt2 = ""
  for i in txt:
    if i in "eaiouAEIOU":
      txt1 += i
    else:
      txt2+= i
  return txt1+txt2

