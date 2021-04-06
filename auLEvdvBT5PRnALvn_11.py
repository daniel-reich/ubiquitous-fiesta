
from string import ascii_lowercase as al
def mirror_cipher(message, key=al):
  message, key = message.lower(), key.lower()
  result = ""
  for letter in message:
    if not letter in key:
      result += letter
    else:
      index = key.find(letter)
      mirror = key[-index-1]
      result += mirror
  return result

