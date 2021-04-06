
def mirror_cipher(message, key = "abcdefghijklmnopqrstuvwxyz"):
  res = ""
  for c in message.lower():
    i = key.find(c)
    if i == -1:
      res += c
      continue
      
    res += key[len(key) - 1 - i]
  
  return res

