
def encrypt(key, message):
  key = [key[i:i+2] for i in range(0,len(key),2)]
  message = list(message)
  for i in range(len(message)):
    for j in key:
      if message[i] in j:
        message[i] = [k for k in j if k!=message[i]][0]
        break
  return ''.join(message)

