
def dial(txt):
  letters = 'abcdefghijklmnopqrstuvwxyz'
  numbers = '22233344455566677778889999'
  return txt.lower().translate(str.maketrans(letters,numbers))

