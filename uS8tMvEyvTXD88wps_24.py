
def reverse(txt):
  
  if " " in txt:
    txt = txt.split()
  else:
    if len(txt) >= 5:
      return txt[::-1]
    else:
      return txt
  
  result = ""
  for word in txt:
    if len(word) >= 5:
      result += word[::-1] + " "
    else:
      result += word + " "
  
  return result[:-1]

