
def direction(lst):
  out_lst = []
  for item in lst:
    word = ""
    for letter in item:
      if letter == ' ':
        word += ' '
      if letter.lower() == 'e':
        word += 'W' if letter == letter.upper() else 'w'
      if letter.lower() == 'a':
        word += 'E' if letter == letter.upper() else 'e'
      if letter.lower() == 's':
        word += 'S' if letter == letter.upper() else 's'
      if letter.lower() == 't':
        word += 'T' if letter == letter.upper() else 't'
    out_lst.append(word)
  return out_lst

