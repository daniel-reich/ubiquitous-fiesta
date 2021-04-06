
def to_snake_case(txt):
  mytxt = ""
  for i in range (len(txt)):
    if (txt[i].isupper()):
      mytxt += "_" + txt[i].lower()
    else:
      mytxt += txt[i]
  return mytxt
​
def to_camel_case(txt):
  mytxt = ""
  Flag = False
  for i in range (len(txt)):
    if (Flag==True):
      mytxt += txt[i].upper()
      Flag = False
    elif (txt[i]=="_"):
      Flag = True
    else:
      mytxt += txt[i]
  return mytxt

