
def alph_num(txt):
  new = ""
  for c in txt:
      if c.isupper():
        new += str(ord(c) - 65)
        new += " "
      elif c.islower():
        new += str(ord(c) - 97)
        new += " "
      else: 
        new+=c
  return new[:-1]

