
def is_in_order(txt):
  for i in range(len(txt) - 1):
    if ord(txt[i]) > ord(txt[i + 1]):
      return False
  return True

