
def count_all(txt):
  letters = sum(i.isalpha() for i in txt)
  digits = sum(i.isdigit() for i in txt)
  return {"LETTERS":  letters, "DIGITS": digits}

