
def simplify(txt):
  new1 = ""
  new2 = ""
  switch = 0
  for i in range(len(txt)):
    if txt[i] == "/":
      switch +=1
    elif switch ==1 :
      new2 = new2+txt[i]
    else:
      new1 = new1+txt[i]
  new1 = int(new1)
  new2 = int(new2)
  if new2 > new1:
    c = new2
    for i in range(new2):
      if c == 1:
        return txt
      if new1%c == 0 and new2%c == 0:
        return "{}/{}".format(int(new1/c),int(new2/c))
      else:
        c-=1
  elif new2 == new1:
    return str(int(new2/new1))
  else:
    if new1%new2 == 0:
      return str(int(new1/new2))
    else:
      c = new1
      for i in range(new1):
        if c == 1:
          return txt
        if new1%c == 0 and new2%c == 0:
          return "{}/{}".format(int(new1/c),int(new2/c))
        c-=1

