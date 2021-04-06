
def reverse(txt):
  return txt[-1] + reverse(txt[:-1]) if txt else ''

