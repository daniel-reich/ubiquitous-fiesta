
def hacker_speak(txt):
  r = {'a':4, 'e':3, 'i':1, 'o':0, 's':5}
  new_str = ""
  for char in txt:
    if char.lower() in r:
      new_str += str(r[char])
    else:
      new_str += char
  return new_str

