
def reverse(txt):
  if txt:
    return txt[-1] + reverse(txt[:-1])
  return txt

