
def first_repeat(chars):
  unique = []
  for c in chars:
    if c in unique:
      return c
    else : unique.append(c)
  return "-1"

