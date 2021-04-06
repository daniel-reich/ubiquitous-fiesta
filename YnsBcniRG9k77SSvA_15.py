
def print_all_groups():
  ref1 = "123456"
  ref2 = "abcde"
  string = ""
  for digit in ref1:
    for letter in ref2:
      string += digit + letter + ", "
  return string[:-2]

