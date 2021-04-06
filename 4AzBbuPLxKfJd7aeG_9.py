
def pairs(s):
  for i in range(0, len(s)-1, 2):
    yield ord(s[i]), s[i+1]
    yield ord(s[i+1]), s[i]
    
​
def encrypt(key, message):
  mapping = {}
  for a, b in pairs(key):
    if a not in mapping:
      mapping[a] = b
  return message.translate(mapping)

