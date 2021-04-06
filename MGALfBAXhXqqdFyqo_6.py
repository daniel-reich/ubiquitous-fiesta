
def atbash(txt):
  return ''.join([chr(155-ord(c)+64*c.islower()) if c.isalpha() else c for c in txt])

