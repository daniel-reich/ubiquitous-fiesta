
def atbash(txt):
  numbers = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18,"T":19,"U":20,"V":21,"W":22,"X":23,"Y":24,"Z":25}
  letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
  
  ans = ""
  for char in txt:
    if char.upper() in letters:
      if char.isupper():
        ans += letters[25-numbers[char]]
      else:
        ans += letters[25-numbers[char.upper()]].lower()
    else:
      ans += char
  
  return ans

