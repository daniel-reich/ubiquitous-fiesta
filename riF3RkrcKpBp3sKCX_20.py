
def cap_space(txt):
  ret_string = ''
  for letter in txt:
    if letter.isupper():
      ret_string += ' ' + letter
    else:
      ret_string += letter
  return ret_string.lower()

