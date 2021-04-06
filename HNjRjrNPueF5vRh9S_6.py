
def hamming_code(message):
  ret = ""
  for char in message:
    a = ord(char)
    b = bin(a).split("b")[1]
    while len(b) < 8:
      b = "0" + b
    for i in b:
      ret = ret + i + i + i
    
  return ret

