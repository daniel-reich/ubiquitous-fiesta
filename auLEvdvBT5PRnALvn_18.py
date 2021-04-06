
alpha = "abcdefghijklmnopqrstuvwxyz"
def mirror_cipher(message,key=alpha):
  rev = key[::-1]
  return "".join(rev[key.index(c)] if c in key else c for c in message.lower())

