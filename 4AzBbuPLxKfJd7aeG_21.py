
def encrypt(key, message):
  dict = {}
  encrypted = [i for i in message]
  for i in range(0, len(key), 2):
    dict.setdefault(key[i:i+1], key[i+1:i+2])
    dict.setdefault(key[i+1:i+2], key[i:i+1])
  for i, a in enumerate(message):
    if a in dict:
      encrypted[i] = dict[a]
  return ''.join(encrypted)

