
def first_repeat(chars):
  return ([i for i in chars if chars.count(i) > 1] + ["-1"])[0]

