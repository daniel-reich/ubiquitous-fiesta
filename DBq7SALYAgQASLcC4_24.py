
def char_count(txt1, txt2):
  var = 0
  for character in txt2:
    if txt1 == character:
      var += 1
    else:
      continue
  return var

