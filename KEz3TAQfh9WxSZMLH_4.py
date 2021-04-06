
def count_all(txt):
  count = {"LETTERS": 0,
           "DIGITS": 0}
  for ch in txt:
    if ch.isalpha():
      count['LETTERS'] += 1
    elif ch.isdigit():
      count['DIGITS'] += 1
  return count

