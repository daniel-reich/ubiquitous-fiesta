
def keyboard_mistakes(txt):
  a_word = list(txt)
  word = ''
  for position, letter in enumerate(a_word):
    if letter == '4':
      word += 'A'
    elif letter == '5':
      word += 'S'
    elif letter == '1':
      word += 'I'
    elif letter == '0':
      word += 'O'
    else:
      word += a_word[position]
  return word

