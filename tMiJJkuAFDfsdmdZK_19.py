
def to_snake_case(txt):
  mystr = ""
  for i in range (len(txt)):
    if (txt[i].isupper()):
      mystr += "_" + txt[i].lower()
    else:
      mystr += txt[i]
  return mystr
​
def to_camel_case(txt):
  mystr = ""
  Flag = False
  for i in range (len(txt)):
    if (Flag==True):
      mystr += txt[i].upper()
      Flag = False
    elif (txt[i]=="_"):
      Flag = True
    else:
      mystr += txt[i]
  return mystr

