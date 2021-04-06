
def count_all(txt):
  a = 0
  b = 0
  for x in range(0, len(txt)):
    if txt[x].isdigit() == True:
      a += 1 
    if txt[x].isalpha() == True:
      b += 1
  mydict = {"LETTERS" : b, "DIGITS" : a}
  return mydict

