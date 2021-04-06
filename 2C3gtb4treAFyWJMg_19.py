
def polybius(text):
  alp = "abcdefghiklmnopqrstuvwxyz"
  num = "12345"
  result = ""
  is_num = bool(text.strip()[0] in num)
  
  if is_num:
    i = 0
    while i < len(text):
      if text[i] == " ":
        result += " "
        i += 1
      else:
        result += alp[(5*(int(text[i])-1))+int(text[i+1])-1]
        i += 2
  else:
    text = text.lower()
    text = text.replace("j","i")
    for i in range(0,len(text)):
      if text[i] == " ":
        result += " "
      elif text[i] in alp:
        result += str(int((alp.index(text[i])//5)+1)) + str(int((alp.index(text[i]) % 5) + 1)) 
  return result

