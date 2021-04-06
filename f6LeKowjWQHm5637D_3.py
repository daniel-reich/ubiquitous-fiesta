
def cap_to_front(s):
  newStr = ""
  for char in s:
    if char.isupper():
      newStr += char
  for char in s:
    if char.islower():
      newStr += char
  return newStr

