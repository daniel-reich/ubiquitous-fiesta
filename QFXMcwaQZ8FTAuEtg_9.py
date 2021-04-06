
def counterpartCharCode(char):
  print(char)
  if not char.isalpha():
    return ord(char)
  else:
    return ord(char.swapcase())

