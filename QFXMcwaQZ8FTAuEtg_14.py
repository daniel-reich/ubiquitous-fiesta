
def counterpartCharCode(char):
  if ord(char) >= 65 and ord(char) <= 90:
    return ord(char) + 32
  elif ord(char) >= 97 and ord(char) <= 122:
    return ord(char) - 32
  else: 
    return ord(char)

