
def caesar_cipher(s, k):
  letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
  Caps =  ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
  new = ""
  for x in s:
    count = 0
    i = 1
    if x.upper() != x:
      for y in range(0,len(letters)):
        if letters[y] == x:
          if y+k >= len(letters):
            while (y+k)- (i*len(letters)) >= len(letters):
              i +=1
            new += letters[(y+k)-(i*len(letters))]
            count += 1
            break
          else:
            new += letters[(y+k)]
            count += 1
            break
    if x.upper() == x:
      for y in range(0,len(letters)):
        if Caps[y] == x:
          if y+k >= len(letters):
            while (y+k)- (i*len(letters)) >= len(letters):
              i +=1
            new += Caps[y+k-(i*len(letters))]
            count += 1
            break
          else:
            new += Caps[y+k]
            count += 1
            break
    if count == 0:
      new += x
  return new

