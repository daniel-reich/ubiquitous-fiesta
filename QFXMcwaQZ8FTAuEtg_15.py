
def counterpartCharCode(char):
  print(char)
  if char.islower():
    print("is_lower()")
    return ord(char.upper())
  else:
    print("is_upper()")
    return ord(char.lower())

