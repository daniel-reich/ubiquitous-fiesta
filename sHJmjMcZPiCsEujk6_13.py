
def pilish_string(txt):
  pi = [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,0]
  str = ""
  for i in pi:
    if txt == "":
      return str
    a = i
    while a > 0:
      if txt == "":
        str += recover
      else:
        str += txt[0]
        recover = txt[0]
        txt = txt[1:]
      a -= 1
    if txt != "":
      str += " "
    if i == 0:
      str = str[0:-2]
  return str

