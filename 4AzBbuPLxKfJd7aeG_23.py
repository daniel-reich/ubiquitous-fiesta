
def encrypt(key, message):
  parts = [key[i:i+2] for i in range(0, len(key), 2)]
  encrypted_message = ''
  for letter in message:
    found = False
    for part in parts:
      if letter in part:
        encrypted_message += part[abs(part.index(letter) - 1)]
        found = True
        break
    if not found: encrypted_message += letter
  
  return encrypted_message

