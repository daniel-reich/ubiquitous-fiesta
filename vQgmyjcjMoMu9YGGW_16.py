
def simplify(txt):
  repeat = True
  txt = txt.split("/")
  a, b = int(txt[0]), int(txt[1])
  if int(a / b) == a / b:
    return (str(int(a / b)))
  
  while repeat:
    repeat = False
    for i in range(2, a + 1):
      if (int(a / i) == a / i) and (int(b / i) == b / i):
        a = int(a / i)
        b = int(b / i)
        repeat = True
​
  return (str (a) + "/" + str(b))

