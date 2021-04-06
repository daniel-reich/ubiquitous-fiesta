
def encrypt(word):
​
  word = word[::-1]
  encryptStr = ""
  
  for char in word:
    if char == "a":
      encryptStr += "0"
    elif char == "e":
      encryptStr += "1"
    elif char == "o":
      encryptStr += "2"
    elif char == "u":
      encryptStr += "3"
    else:
      encryptStr += char
  
  encryptStr += "aca"
  return encryptStr

