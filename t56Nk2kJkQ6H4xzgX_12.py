
def swap_xy(txt):
  chars = [",","(", ")"]
  for char in chars:
    txt = txt.replace(char,"")
  txt = txt.split(" ")
  num1 = txt[0]
  num2 = txt[1]
  num3 = txt[2]
  num4 = txt[3]
  
  
  
  
  return "({}, {}), ({}, {})".format(num2,num1,num4,num3)

