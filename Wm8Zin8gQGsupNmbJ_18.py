
def binary_conversion(txt):
  if txt == "":
    return ""
  else:
    lst = []
    for t in range(0,len(txt),8):
      lst.append(txt[t:t+8])
  
  text = ""
  for l in lst:
    text += chr(int(l, 2))
  
  return text

