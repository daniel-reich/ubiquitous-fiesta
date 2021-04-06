
def is_in_order(txt):
  for i in range(len(txt) - 1):
    if txt[i] > txt[i + 1]:
      return False
  return True

