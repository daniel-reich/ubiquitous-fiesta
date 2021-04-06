
def atbash(txt):
  down = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
  up = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
  ata = ""
  i = 0
  while i < len(txt):
    if txt[i].islower():
      x = 25 - down.index(txt[i])
      ata = ata + down[x]
    elif txt[i].isupper():
      x = 25 - up.index(txt[i])
      ata = ata + up[x]
    else: 
      ata = ata + txt[i]
    i += 1
  return ata

