
def true_alphabetic(txt):
  x  = [len(i) for i in txt.split(" ")]
  txt = txt.replace(" ", "")
  print (x)
  y = sorted(txt, key=lambda x:ord(x))
  a = []
  print (y)
  b = ""
  p = 0
  for i in y:
    if x[p] == len(b):
      a.append(b)
      b = ""
      b += i
      p += 1
    else:
      b += i
  a.append(b)
  return " ".join(a)

