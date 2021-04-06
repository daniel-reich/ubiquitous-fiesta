
def return_unique(lst):
  result = []
  for char in lst:
    if lst.count(char) < 2:
      result.append(char)
  return result

