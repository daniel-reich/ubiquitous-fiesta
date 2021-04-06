
def first_repeat(chars):
  seen = set()
  for c in chars:
    if c in seen:
      return c
    else: seen.add(c)
  return "-1"

