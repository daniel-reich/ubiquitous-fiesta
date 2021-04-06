
def keyboard_shortcut(txt):
  txt = txt.split()
  res = [] 
  clipboard = []
  while txt.count("Ctrl") > 0 : txt.remove("Ctrl")
  while txt.count("+") > 0 : txt.remove("+")
  for i in range(len(txt)) :
    if txt[i] == "C" :
      clipboard = res
    elif txt[i] == "V" :
      res += clipboard
    else :
      res.append(txt[i])
  return " ".join(res)

