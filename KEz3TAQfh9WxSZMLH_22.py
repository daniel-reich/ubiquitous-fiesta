
def count_all(txt):
  lil_dicty = {
  "LETTERS": 0,
  "DIGITS": 0
  }
  for i in txt:
    if i.isdigit():
      lil_dicty["DIGITS"] += 1
    elif i.isalpha():
      lil_dicty["LETTERS"] += 1
  return lil_dicty

