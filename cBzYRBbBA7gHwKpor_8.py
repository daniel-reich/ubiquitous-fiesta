
def secret_password(message):
  import string
  output = ""
  if len(message) != 9 or not all([i in string.ascii_lowercase for i in message]):
    return "BANG! BANG! BANG!"
  else:
    for i in range(5,2,-1):
      output += message[i]
    for i in range(6,9):
      output += string.ascii_lowercase[(string.ascii_lowercase.index(message[i])+1)%26]
    output += str(string.ascii_lowercase.index(message[0]) + 1)
    output += message[1]
    output += str(string.ascii_lowercase.index(message[2]) + 1)
    return output

