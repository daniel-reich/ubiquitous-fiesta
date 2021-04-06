
def counterpartCharCode(char):
  if 65 <= ord(char) <= 90:
    return ord(char) + 32
  elif 97 <= ord(char) <= 123:
    return ord(char) - 32
  else: return ord(char)

