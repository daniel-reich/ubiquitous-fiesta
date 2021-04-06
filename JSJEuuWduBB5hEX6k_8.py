
def XO(text):
  xs = 0
  os = 0
  for each in text:
    if each == "x" or each == "X":
      xs += 1
    elif each == "o" or each == "O":
      os += 1
  return xs==os

