
def replace(txt, r):
  mystr = ""
  for i in range (len(txt)):
    if (ord(txt[i])>=ord(r[0]) and ord(txt[i])<=ord(r[2])):
      mystr += "#"
    else:
      mystr += txt[i]
  return mystr

