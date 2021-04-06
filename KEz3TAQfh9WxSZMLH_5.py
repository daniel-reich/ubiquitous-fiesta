
def count_all(txt):
  count = 0
  digit = 0
  for char in txt:
    if char.isdigit():
      digit += 1
    elif char.isalpha() and char not in " ":
      count += 1
  return {"LETTERS": count, "DIGITS": digit}

