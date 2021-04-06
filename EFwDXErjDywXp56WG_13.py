
def is_in_order(txt):
  separator = ""
  list_test = separator.join(sorted(txt))
  if list_test == txt:
    return True
  else:
    return False

