
def mirror_cipher(message,key="abcdefghijklmnopqrstuvwxyz"):
  return message.lower().translate(str.maketrans(key,key[::-1]))

