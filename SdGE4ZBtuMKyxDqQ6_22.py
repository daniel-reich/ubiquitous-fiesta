
def first_repeat(chars):
  for i in chars:
    if chars.count(i) > 1: 
      return i
  return "-1"

