
import string
def to_snake_case(txt):
  newstring = ""
  for i in txt:
    if i in string.ascii_uppercase:
      newstring += "_"
      newstring += i.lower()
    else:
      newstring += i
  return newstring
  
def to_camel_case(txt):
  splitstr = txt.split("_")
  newstring = ""
  c2 = 0
  for i in splitstr:
    c = 0
    for x in i:
      print(":")
      if c == 0 and c2 != 0:
        print(x.upper())
        newstring += x.upper()
      else:
        print(x)
        newstring += x
      c += 1
    c2 += 1
  return newstring

