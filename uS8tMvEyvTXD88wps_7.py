
def reverse(txt):
  list_letters = txt.split(' ')
  return ' '.join([x[::-1] if len(x) >= 5 else x for x in list_letters])

