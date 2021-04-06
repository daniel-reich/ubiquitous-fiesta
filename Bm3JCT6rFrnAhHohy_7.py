
def alphabet_index(txt):
  return_string = ""
  for letter in txt.lower():
    if ord(letter) >= 97 and ord(letter) <= 122:
      return_string = return_string + str(ord(letter)-96) + " "
  return return_string[:-1]

