
def keyboard_mistakes(txt):
  return ''.join('A' if x == '4' else 'O' if x == '0' else 'S' if x == '5' else 'I' if x == '1' else x for x in txt)

