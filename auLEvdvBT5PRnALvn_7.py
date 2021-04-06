
def mirror_cipher(message, key="abcdefghijklmnopqrstuvwxyz"):
  return "".join(key[-key.find(c) - 1] if c in key else c for c in message.lower())

