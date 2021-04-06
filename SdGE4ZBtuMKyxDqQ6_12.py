
def first_repeat(chars):
  for x in chars:
    if chars.count(x) > 1:
      return x
  return '-1'

