
def count_all(txt):
  result = {"LETTERS": 0, "DIGITS": 0}
  for c in txt:
    if(c.isdigit()):
      result["DIGITS"] += 1
    elif(c.isalpha()):
      result["LETTERS"] += 1
​
  return result

