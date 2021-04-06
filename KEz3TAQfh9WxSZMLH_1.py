
def count_all(txt):
  return {"LETTERS": sum(c.isalpha() for c in txt),
          "DIGITS": sum(c.isdigit() for c in txt)}

