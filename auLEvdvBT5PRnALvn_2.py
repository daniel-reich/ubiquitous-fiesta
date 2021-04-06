
def mirror_cipher(message,key="abcdefghijklmnopqrstuvwxyz"):
  mirrored = dict(zip(key,key[::-1]))
  return "".join(mirrored.get(i.lower(),i.lower()) for i in message)

