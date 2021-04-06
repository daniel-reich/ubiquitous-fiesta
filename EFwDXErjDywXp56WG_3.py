
def is_in_order(txt):
  for i in range(1, len(txt)):
    if txt[i] < txt[i-1]:
      return False
  return True

