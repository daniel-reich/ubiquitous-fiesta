
def encrypt(plncode, pad):
  message = '63719'
  newpad = pad[5:]
  for i in range(len(plncode)):
    nr = int(plncode[i]) - int(newpad[i])
    if nr < 0:
      message += str(nr % 10)
    elif nr > 9:
      message += str(nr / 10)
    else:
      message += str(nr)
  return message
  
​
def decrypt(cypcode, pad):
  message = '63719'
  if cypcode[:5] != message or pad[:5] != message:
    return "Error: Key IDs don't match."
  else:
    message = ''
    cypcode = cypcode[5:]
    pad = pad[5:]
    for i in range(len(cypcode)):
      nr = int(cypcode[i]) + int(pad[i])
      if nr > 9:
        message += str(int(nr % 10))
      else:
        message += str(nr)
  return message

