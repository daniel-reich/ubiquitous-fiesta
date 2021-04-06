
def count_all(txt):
  result = {"LETTERS":  0, "DIGITS": 0}
  for i in txt:
    if i.isdigit():
      result['DIGITS'] += 1
    elif i.isalpha():
      result['LETTERS'] += 1
  return result

