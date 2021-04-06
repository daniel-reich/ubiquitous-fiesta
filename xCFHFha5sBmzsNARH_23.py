
def reverse(txt):
  if not txt:
    return ""
  return txt[-1] + reverse(txt[:-1])

