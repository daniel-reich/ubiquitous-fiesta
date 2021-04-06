
def apocalyptic(n):
  txt = str(2**n)
  for i in range(len(txt)-2):
    if txt[i:i+3] == "666":
      return  "Repent! " + str(i) + " days until the Apocalypse!"
  return "Crisis averted. Resume sinning."

