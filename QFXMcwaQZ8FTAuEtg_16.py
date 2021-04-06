
def counterpartCharCode(char):
  if char.islower():
    return (ord(char) - 32)
  elif char.isupper():
    return (ord(char) + 32)
  else: 
    return ord(char)

