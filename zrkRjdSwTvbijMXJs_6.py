
def encrypt(plncode, pad):
  result = pad[:5]
  for i in range(len(plncode)):
    x = int(plncode[i]) - int(pad[i+5]) + 10
    result += str(x)[-1]
  return result
​
def decrypt(cypcode, pad):
  if cypcode[:5] != pad[:5]: return "Error: Key IDs don't match."
  result = ""
  for i in range(5,len(cypcode)):
    x = int(cypcode[i]) +int(pad[i])
    result += str(x)[-1]
  return result

