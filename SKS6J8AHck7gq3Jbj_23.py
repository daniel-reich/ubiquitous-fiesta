
def tidy_books(lst):
  result = []
  for item in lst:
    string = item[0].strip()
    result.append([string[:string.index("-") - 1], string[string.index("-") + 2:]])
  return result

