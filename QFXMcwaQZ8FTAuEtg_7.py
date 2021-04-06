
def counterpartCharCode(char):
  if char.isupper():
    return ord(char.lower())
  elif char.islower():
    return ord(char.upper())
  else:
    return ord(char)

