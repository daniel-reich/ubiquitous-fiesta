
def mirror_cipher(message,key="abcdefghijklmnopqrstuvwxyz"):
  return ''.join([i if i not in key else key[::-1][key.find(i)] for i in message.lower()])

