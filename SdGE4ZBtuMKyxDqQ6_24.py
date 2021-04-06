
def first_repeat(chars):
  for letter in chars:
    if chars.count(letter) >= 2:
      return letter
  return str(-1)

