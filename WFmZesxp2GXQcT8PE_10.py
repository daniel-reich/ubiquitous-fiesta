
def digital_cipher(message, key):
  return [sum((ord(x) - 96, int(y))) for x, y in zip(message, str(key) * ((len(message) // len(str(key))) + 1))]

