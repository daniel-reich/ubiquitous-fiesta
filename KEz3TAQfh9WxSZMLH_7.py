
def count_all(txt):
  result = {"LETTERS": 0, "DIGITS": 0}
  
  for x in txt:
    if x.isdigit():
      result["DIGITS"] += 1
    elif x.isalpha():
      result["LETTERS"] += 1
  return result

