
def first_non_repeated_character(txt):
  found = [val for val in txt if txt.count(val) == 1]
  return False if not found else found[0]

