
def count_characters(lst):
  result = 0
  for elem in lst:
    for char in elem:
      result += 1
  return result

